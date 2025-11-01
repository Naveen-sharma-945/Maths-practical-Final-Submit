import numpy as np

# --- Step 1: Input Vectors ---
# Example: Three vectors in R^3
v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
v3 = np.array([1, 0, 1])

# Combine them as columns of a matrix
A = np.column_stack((v1, v2, v3))
print("Matrix formed by given vectors:\n", A)

# --- Step 2: Check Linear Dependence ---
# Find rank of matrix
rank = np.linalg.matrix_rank(A)

print("\nRank of matrix =", rank)
if rank < A.shape[1]:
    print("=> The vectors are LINEARLY DEPENDENT.")
else:
    print("=> The vectors are LINEARLY INDEPENDENT.")

# --- Step 3: Generate a Linear Combination ---
# Let's take coefficients a1, a2, a3
a1, a2, a3 = 2, -1, 3
linear_combination = a1*v1 + a2*v2 + a3*v3
print("\nLinear combination = 2*v1 - v2 + 3*v3 = ", linear_combination)

# --- Step 4: Find Transition Matrix ---
# Suppose we have two bases for R^2 for demonstration
B1 = np.array([[1, 0],
               [0, 1]])   # Standard basis
B2 = np.array([[2, 1],
               [1, 1]])   # Another basis

# Transition matrix from B1 to B2:
P = np.dot(np.linalg.inv(B2), B1)
print("\nTransition matrix from B1 to B2:\n", P)
