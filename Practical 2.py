import numpy as np
from sympy import Matrix

# --- Step 1: Create a matrix ---
A = Matrix([[2, 4, -2],
            [4, 9, -3],
            [-2, -3, 7]])

print("Original Matrix:")
print(A)

# --- Step 2: Convert the matrix to Row Echelon Form (REF) ---
A_echelon = A.echelon_form()
print("\nMatrix in Row Echelon Form:")
print(A_echelon)

# --- Step 3: Find the Rank of the matrix ---
rank = A.rank()
print("\nRank of the Matrix:", rank)
