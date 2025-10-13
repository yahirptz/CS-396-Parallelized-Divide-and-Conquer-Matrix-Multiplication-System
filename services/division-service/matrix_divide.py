# Divide entire matrix into one row and one column at a time, and send
# each row and column to matrix_multiply container(s)

# Take in two matrices and divide it into one row and one column.
# row_mat: the matrix in which only rows are used to multiply into a column
# col_mat: the matrix in which only columns are used to multiply into a row

def divide(row_mat, col_mat):
    for i in range(1, len(row_mat)+1):
        index = i % 10000
        row = row_mat[i]
        for j in range(1, len(col_mat)+1):
            column = col_mat[j]
            # Send to multiplier container
            
        
