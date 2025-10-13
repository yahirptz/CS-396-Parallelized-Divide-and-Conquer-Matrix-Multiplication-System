from enum import Enum
#Defines all possible message types
class MessageType(Enum):
    """All the different types of messages we can send"""
    RESULT = "RESULT"              # When multiplication finishes, send result here
    INIT_MATRIX = "INIT_MATRIX"    # Tells aggregation what size matrix to create
    GET_MATRIX = "GET_MATRIX"      # Ask aggregation for the final matrix
    STATUS = "STATUS"              # Check how many results we've received




def create_result_message(row_index: int, col_index: int, value: float):
    """
    Christian's multiplication service calls this to send you a result
    Example: create_result_message(0, 5, 42.5)
    Means: row 0, column 5 = 42.5
    """
    return {
        "type": "RESULT",
        "row_index": row_index,      # Which row of final matrix
        "col_index": col_index,      # Which column of final matrix
        "value": value               # The calculated number
    }


def create_init_message(rows: int, cols: int):
    """
    GUI calls this first to tell you the size of the result matrix
    Example: create_init_message(100, 100)
    Means: create a 100x100 matrix to store results
    """
    return {
        "type": "INIT_MATRIX",
        "rows": rows,                # Number of rows in result
        "cols": cols                 # Number of columns in result
    }


def create_status_request():
    """
    GUI can call this to ask "how many results have you received?"
    """
    return {
        "type": "STATUS"
    }


def create_status_response(received: int, total: int):
    """
    You send this back when GUI asks for status
    Example: create_status_response(50, 100)
    Means: received 50 out of 100 results
    """
    return {
        "type": "STATUS",
        "received": received,        # How many results collected so far
        "total": total,              # How many results expected total
        "complete": received == total  # True when done
    }


def create_get_matrix_request():
    """
    GUI calls this when it wants the final completed matrix
    """
    return {
        "type": "GET_MATRIX"
    }


def create_matrix_response(matrix: list):
    """
    You send this back to GUI with the completed matrix
    Example: create_matrix_response([[1, 2], [3, 4]])
    """
    return {
        "type": "MATRIX_RESPONSE",
        "matrix": matrix             # The final matrix
    }