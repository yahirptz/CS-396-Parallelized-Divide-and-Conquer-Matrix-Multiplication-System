# The logic of aggregation works like this:
# The element must be aggregated at the coordinate x, y, where x is the
# index of the multiplied row and y is the index of the multiplied column.
# (Ex: element x1, y1 of the matrix will be the multiplication of row 1 and column 1.)
# (element x1, y2 of the matrix will be the multiplication of row 1 and column 2.)
# (and so on and so forth.)

import sys
import os
import socket
import json
import threading

shared_path = os.path.join(os.path.dirname(__file__), '..', '..', 'shared')
sys.path.insert(0, shared_path)

from message_types import create_status_response, create_matrix_response

# microservice variable "current_matrix" that has all finished elements up to that point
current_matrix = []
matrix_rows = 0
matrix_cols = 0
results_received = 0
total_results = 0


def initialize_matrix(rows, cols):
    #creates empyy matrix to store the result
    global current_matrix, matrix_rows, matrix_cols, total_results, results_received
    
    matrix_rows = rows
    matrix_cols = cols
    total_results = rows * cols
    results_received = 0
    
    # Create empty matrix filled with zeros
    current_matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0.0)
        current_matrix.append(row)
    
    print(f"Matrix initialized: {rows}x{cols}, expecting {total_results} results")


def add_result(row_index, col_index, value):
    # Add one result to the matrix Called when multiplication worker sends a result
    global current_matrix, results_received
    
    # Place result in correct position
    current_matrix[row_index][col_index] = value
    results_received += 1
    
    print(f"Added result at [{row_index}][{col_index}] = {value}")
    print(f"Progress: {results_received}/{total_results}")


def get_status():
    # this checks how many results have been received 
    status = create_status_response(results_received, total_results)
    return status


def get_final_matrix():
    #returs the final matrix 
    response = create_matrix_response(current_matrix)
    response['received'] = results_received
    response['total'] = total_results
    response['complete'] = (results_received == total_results)
    return response


def is_complete():
   #checks if all results have been recieved
    return results_received == total_results


def handle_client(client_socket, address):
    #handles incoming TCP connection from worker
    try:
        # Receive data from client
        data = client_socket.recv(4096)
        
        if data:
            # Convert bytes to JSON to dictionary
            message = json.loads(data.decode('utf-8'))
            message_type = message.get('type')
            
            if message_type == 'INIT_MATRIX':
                # Initialize the matrix
                rows = message['rows']
                cols = message['cols']
                initialize_matrix(rows, cols)
                
                # Send response back
                response = {"status": "initialized"}
                client_socket.send(json.dumps(response).encode('utf-8'))
                
            elif message_type == 'RESULT':
                # Receive a result from worker
                row = message['row_index']
                col = message['col_index']
                value = message['value']
                
                # Use existing function to add result
                add_result(row, col, value)
                
                # Send acknowledgment
                response = {"status": "received"}
                client_socket.send(json.dumps(response).encode('utf-8'))
                
            elif message_type == 'GET_MATRIX':
                # Send completed matrix
                response = get_final_matrix()
                client_socket.send(json.dumps(response).encode('utf-8'))
                
            elif message_type == 'STATUS':
                # Send status
                response = get_status()
                client_socket.send(json.dumps(response).encode('utf-8'))
    
    except Exception as e:
        print(f"Error handling client {address}: {e}")
    
    finally:
        client_socket.close()


def start_tcp_server():
    #starts TCP server to listen for connections
    host = '0.0.0.0'
    port = 5003
    
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind to port
    server_socket.bind((host, port))
    
    # Listen for connections
    server_socket.listen(5)
    print(f"Aggregation Service listening on {host}:{port}")
    print("Waiting for connections from workers...")
    
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")
        
        # Handle each connection in separate thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()


if __name__ == '__main__':
    print("=" * 50)
    print("Starting Aggregation Service")
    print("=" * 50)
    start_tcp_server()