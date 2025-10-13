# Taking in one row and one column, multiply them together.
# The result is one (1) element, which will then be put into the completed matrix.

def multiply_row_column(row, column):
    result = 0
    for i in range(len(row)):
        result += row[i] * column[i]
    