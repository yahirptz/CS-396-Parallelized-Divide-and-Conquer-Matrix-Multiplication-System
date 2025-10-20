import socket
import json
import threading
import os
import sys
shared_path = os.path.join(os.path.dirname(__file__), '..', '..', 'shared')
sys.path.insert(0, shared_path)
from message_types import create_divide_message

def start_tcp_server():
    host = '0.0.0.0'
    port = 5001 # Port for division service
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to port
    server_socket.bind((host, port))
    server_socket.listen(5)

def handle_client(client_socket, address):
    try:
        while True:
            # Receive data
            data = client_socket.recv(4096)
            if not data:
                break

            # Decode JSON message
            message = json.loads(data.decode('utf-8'))
            print(f"Received message from {address}: {message}")

            # Process the message based on its type
            if message['type'] == 'DIVIDE':
                row_matrix = message['matrix1']
                col_matrix = message['matrix2']
                divide(row_matrix, col_matrix)

    except Exception as e:
        print(f"Error handling client {address}: {e}")

    finally:
        client_socket.close()


def send_to_multiplication_service(message, host, port):
    """
    Sends a JSON message to the multiplication service.

    Parameters:
        message (dict): The message to send.
        host (str): The hostname or IP address of the multiplication service.
        port (int): The port number of the multiplication service.

    Returns:
        None
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        client_socket.sendall(json.dumps(message).encode('utf-8'))
        print(f"Sent data to {host}:{port} - {message}")

    except Exception as e:
        print(f"Error sending data to {host}:{port} - {e}")

    finally:
        client_socket.close()

def divide(row_mat, col_mat):
    """
    Divides two matrices into individual rows and columns for multiplication.

    Parameters:
        row_mat (list of list of numbers): The matrix whose rows are used for multiplication.
        col_mat (list of list of numbers): The matrix whose columns are used for multiplication.

    Returns:
        None
    """
    for i in range(len(row_mat)):
        row = row_mat[i]
        for j in range(len(col_mat)):
            column = [col[j] for col in col_mat]
            # Save the row and column for processing
            message = create_divide_message(row, column, i, j)
            # Send to multiplication container
            send_to_multiplication_service(message, '0.0.0.0', 5002)
            
if __name__ == "__main__":
    print("=" * 50)
    print("Starting Division Service")
    print("=" * 50)
    start_tcp_server()


    # Test example (uncomment to run test)
    # Example matrices
    """
    row_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    col_matrix = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    divide(row_matrix, col_matrix)
    """
