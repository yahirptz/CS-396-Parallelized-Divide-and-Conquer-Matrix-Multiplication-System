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
            print(f"Row {i+1}: {row}, Column {j+1}: {column}")
            
if __name__ == "__main__":
    # Example matrices
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
