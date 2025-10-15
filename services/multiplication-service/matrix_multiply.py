import sys
import os
sys.path.append('C:/Users/jessc/OneDrive/Documents/Test/CS-396-Parallelized-Divide-and-Conquer-Matrix-Multiplication-System/shared')
from message_types import MessageType

# Taking in one row and one column, multiply them together.
# The result is one (1) element, which will then be put into the completed matrix.

def multiply_row_column(row, column, row_index, col_index):
    """
    Multiply a row and column and create a result message
    
    Args:
        row: List of numbers representing a row
        column: List of numbers representing a column
        row_index: Index of the row in the final matrix
        col_index: Index of the column in the final matrix
    
    Returns:
        dict: Result message containing position and calculated value
    """
    result = 0
    for i in range(len(row)):
        result += row[i] * column[i]
    
    # Create message with result position and value
    return MessageType.create_result_message(row_index, col_index, result)

if __name__ == "__main__":
    # Test example
    row = [1, 2, 3]
    column = [4, 5, 6] 
    message = multiply_row_column(row, column, 0, 0)
    print(f"Result message: {message}")
    # Should print: {'type': 'RESULT', 'row_index': 1, 'col_index': 1, 'value': 32}