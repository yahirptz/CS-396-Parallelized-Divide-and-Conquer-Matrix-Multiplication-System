# Divide entire matrix into one row and one column at a time, and send
# each row and column to matrix_multiply container(s)

# Take in two matrices and divide it into one row and one column.
# row_mat: the matrix in which only rows are used to multiply into a column
# col_mat: the matrix in which only columns are used to multiply into a row

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
            column = col_mat[j]
            # Send to multiplier container
            
        
