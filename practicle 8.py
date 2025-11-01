# Practical: Find Orthonormal Basis using Gram–Schmidt Process
# Author: Your Name
import numpy as np

# --- Step 1: Input vectors ---
# Example: Three vectors in R^3
v1 = np.array([1, 1, 0], dtype=float)
v2 = np.array([1, 0, 1], dtype=float)
v3 = np.array([0, 1, 1], dtype=float)

# Combine into a matrix
V = np.column_stack((v1, v2, v3))
print("Given vectors:\n", V)

# --- Step 2: Gram-Schmidt Process ---
def gram_schmidt(V):
    n = V.shape[1]       # number of vectors
    U = np.zeros_like(V) # to store orthogonal vectors
    
    for i in range(n):
        # Start with the original vector
        U[:, i] = V[:, i]
        
        # Subtract projections onto previous U vectors
        for j in range(i):
            proj = np.dot(V[:, i], U[:, j]) / np.dot(U[:, j], U[:, j]) * U[:, j]
            U[:, i] -= proj
            
    return U

U = gram_schmidt(V)
print("\nOrthogonal basis:\n", U)

# --- Step 3: Normalize the vectors to get Orthonormal basis ---
def normalize(U):
    for i in range(U.shape[1]):
        U[:, i] = U[:, i] / np.linalg.norm(U[:, i])
    return U

Q = normalize(U)
print("\nOrthonormal basis:\n", Q)
