import sys
import os
import socket
import threading
import json
shared_path = os.path.join(os.path.dirname(__file__), '..', '..', 'shared')
sys.path.insert(0, shared_path)

from message_types import create_result_message

# Taking in one row and one column, multiply them together.
# The result is one (1) element, which will then be put into the completed matrix.

def send_to_aggregate(message, host, port):
    # Send a JSON message to specified host and port
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Try to connect and send data
    try:
        client_socket.connect((host, port))
        client_socket.sendall(json.dumps(message).encode('utf-8'))
        print(f"Sent data to {host}:{port} - {message}")
    except Exception as e:
        print(f"Error sending data to {host}:{port} - {e}")

# Handle incoming connections from division workers
def handle_client(client_socket, address):
    # Handle incoming messages from a connected client
    with client_socket:
        print(f"Handling client {address}")
        while True:
            try:
                #Receive data from client
                data = client_socket.recv(4096)
                if not data:
                    print(f"Client {address} disconnected")
                    break
                
                # Decode JSON message
                message = json.loads(data.decode('utf-8'))
                print(f"Received message from {address}: {message}")
                
                # Process the message based on its type
                if message['type'] == 'MULTIPLY':
                    row = message['row']
                    column = message['column']
                    row_index = message['row_index']
                    col_index = message['col_index']
                    
                    # Perform multiplication
                    result_message = multiply_row_column(row, column, row_index, col_index)
                    
                    # Send result to aggregation service
                    send_to_aggregate(result_message,'0.0.0.0', 5003)
                    client_socket.sendall(json.dumps(result_message).encode('utf-8'))
                    print(f"Sent result to {address}: {result_message}")

                    # Close connection after processing
                    client_socket.close()
                    print(f"Closed connection with {address} after processing")
                
            except Exception as e:
                print(f"Error handling client {address}: {e}")
                break

def start_tcp_server():
#starts TCP server to listen for connections
    host = '0.0.0.0'
    port = 5002
    
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind to port
    server_socket.bind((host, port))
    
    # Listen for connections
    server_socket.listen(5)
    print(f"Aggregation Service listening on {host}:{port}")
    print("Waiting for connections from workers")
    
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")
        
        # Handle each connection in separate thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

def multiply_row_column(row, column, row_index, col_index):
    """
    Multiply a row and column and create a result message
    
    Args:
        row: List of numbers representing a row
        column: List of numbers representing a column
        row_index: Index of the row in the final matrix
        col_index: Index of the column in the final matrix
    
    Returns:
        Result of multiplication as a message dictionary with row index, column index, and value
    """
    result = 0
    for i in range(len(row)):
        result += row[i] * column[i]
    
    # Create message with result position and value
    return create_result_message(row_index, col_index, result)

if __name__ == "__main__":
    print("=" * 50)
    print("Starting Multiplication Service")
    print("=" * 50)
    start_tcp_server()

    # Test example (uncomment to run test)
    #row = [1, 2, 3]
    #column = [4, 5, 6] 
    #message = multiply_row_column(row, column, 0, 0)
    #print(f"Result message: {message}")
    # Should print: {'type': 'RESULT', 'row_index': 1, 'col_index': 1, 'value': 32}