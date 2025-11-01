import numpy as np

# --- Step 1: Create a square matrix ---
A = np.array([[2, 3, 1],
              [4, 1, -3],
              [1, 2, 0]])

print("Original Matrix A:", A)

# --- Step 2: Determinant ---
det = np.linalg.det(A)
print("Determinant of A:", round(det, 2))

# --- Step 3: Function to find cofactor matrix ---
def cofactor_matrix(matrix):
    n = matrix.shape[0]
    cof = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            # Minor: remove row i and column j
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cof[i][j] = ((-1) ** (i + j)) * np.linalg.det(minor)
    return cof

C = cofactor_matrix(A)
print("Cofactor Matrix:", C)

# --- Step 4: Adjoint (Transpose of cofactor matrix) ---
adj = C.T
print("Adjoint :", adj)

# --- Step 5: Inverse using formula ---
if det != 0:
    inv = adj / det
    print("Inverse of A (Adjoint / Determinant):", np.round(inv, 2))
else:
    print("Matrix is Singular (Determinant = 0), No Inverse Exists.")
