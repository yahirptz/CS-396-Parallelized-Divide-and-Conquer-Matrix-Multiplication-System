# The logic of aggregation works like this:
# The element must be aggregated at the coordinate x, y, where x is the
# index of the multiplied row and y is the index of the multiplied column.
# (Ex: element x1, y1 of the matrix will be the multiplication of row 1 and column 1.)
# (element x1, y2 of the matrix will be the multiplication of row 1 and column 2.)
# (and so on and so forth.)

import sys
import os

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


# Test the aggregation logic
if __name__ == '__main__':
    print("Testing aggregation logic...")
    
    # Test with small 3x3 matrix
    initialize_matrix(3, 3)
    
    # Simulate receiving results
    add_result(0, 0, 15.0)
    add_result(0, 1, 18.0)
    add_result(0, 2, 21.0)
    add_result(1, 0, 42.0)
    add_result(1, 1, 54.0)
    add_result(1, 2, 66.0)
    add_result(2, 0, 69.0)
    add_result(2, 1, 90.0)
    add_result(2, 2, 111.0)
    
    # Check status
    status = get_status()
    print(f"\nStatus: {status}")
    
    # Get final matrix
    if is_complete():
        result = get_final_matrix()
        print("\nFinal Matrix:")
        for row in result['matrix']:
            print(row)