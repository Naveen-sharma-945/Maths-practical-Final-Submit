import numpy as np

# --- Step 1: Create a simple vector and matrix ---
# Vector (1D)
vector = np.array([1, 2, 3])
print("Original Vector:\n", vector)

# Matrix (2D)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\nOriginal Matrix:\n", matrix)

# --- Step 2: Transpose ---
vector_T = np.transpose(vector)
matrix_T = np.transpose(matrix)
print("\nTranspose of Vector (Note: same as original since it's 1D):\n", vector_T)
print("\nTranspose of Matrix:\n", matrix_T)

# --- Step 3: Create complex vector/matrix for conjugate transpose ---
complex_vector = np.array([1+2j, 3+4j, 5+6j])
complex_matrix = np.array([[1+2j, 2-1j],
                           [3+4j, 4+0j]])

# --- Step 4: Conjugate transpose (Hermitian transpose) ---
vector_H = np.conjugate(complex_vector).T
matrix_H = np.conjugate(complex_matrix).T

print("\nComplex Vector:\n", complex_vector)
print("Conjugate Transpose (Hermitian) of Vector:\n", vector_H)

print("\nComplex Matrix:\n", complex_matrix)
print("Conjugate Transpose (Hermitian) of Matrix:\n", matrix_H)
