import numpy as np
from scipy.linalg import orth, null_space

# Define your matrix A
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Column space basis (orthonormal columns)
col_space_basis = orth(A)
print("Column space basis:")
print(col_space_basis)

# Row space basis (orthonormal rows)
row_space_basis = orth(A.T)
print("Row space basis:")
print(row_space_basis)

# Null space basis
null_space_basis = null_space(A)
print("Null space basis:")
print(null_space_basis)

# Left null space basis (null space of A transpose)
left_null_space_basis = null_space(A.T)
print("Left null space basis:")
print(left_null_space_basis)

