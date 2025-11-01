# --------------------------------------------------
# Practical 5 : Solve a system of homogeneous equations
# using the Gauss-Jordan method
# --------------------------------------------------

import numpy as np   # we use numpy for matrix operations

# Step 1 : Enter the coefficients of the equations
# Example system:
# 2x +  y - z = 0
# -x + 3y + 2z = 0
# 3x - 2y + 4z = 0

A = np.array([
    [2, 1, -1, 0],   # coefficients and constant term (0)
    [-1, 3, 2, 0],
    [3, -2, 4, 0]
], dtype=float)

# Step 2 : Print the starting (augmented) matrix
print("Initial Augmented Matrix [A | 0]:")
print(A)

# Step 3 : Apply Gauss-Jordan elimination
rows, cols = A.shape

for i in range(rows):
    # make the diagonal element 1
    if A[i, i] == 0:
        # if the pivot is 0, swap with another row
        for j in range(i + 1, rows):
            if A[j, i] != 0:
                A[[i, j]] = A[[j, i]]   # swap
                break

    pivot = A[i, i]
    A[i] = A[i] / pivot   # make pivot = 1

    # make all other elements in that column = 0
    for j in range(rows):
        if j != i:
            factor = A[j, i]
            A[j] = A[j] - factor * A[i]

# Step 4 : Print the final matrix (Reduced Row Echelon Form)
print("\nMatrix after Gauss-Jordan elimination (RREF):")
print(np.round(A, 3))

# Step 5 : Show result meaning
print("\nSince this is a homogeneous system (Ax = 0),")
print("the trivial solution is always x = y = z = 0.")
print("If any row becomes all zeros, then there are infinite solutions.")
