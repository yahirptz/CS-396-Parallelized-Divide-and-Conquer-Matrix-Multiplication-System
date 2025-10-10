# The logic of aggregation works like this:
# The element must be aggregated at the coordinate x, y, where x is the
# index of the multiplied row and y is the index of the multiplied column.
# (Ex: element x1, y1 of the matrix will be the multiplication of row 1 and column 1.)
# (element x1, y2 of the matrix will be the multiplication of row 1 and column 2.)
# (and so on and so forth.)

# microservice variable "current_matrix" that has all finished elements up to that point
current_matrix = []