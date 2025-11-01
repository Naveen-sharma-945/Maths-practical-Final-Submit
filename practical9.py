# Program: Check diagonalizability, find eigenvalues,
#          and verify the Cayley–Hamilton theorem
# Author: Your Name
# Library: NumPy

import numpy as np

# --- Step 1: Input Matrix ---
# You can change this to any square matrix
A = np.array([[4, 1],
              [2, 3]], dtype=float)

print("Given Matrix A:\n", A)

# --- Step 2: Find Eigenvalues and Eigenvectors ---
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues of A:")
print(eigenvalues)

print("\nEigenvectors of A (columns represent eigenvectors):")
print(np.round(eigenvectors, 4))

# --- Step 3: Check Diagonalizability ---
# A matrix is diagonalizable if eigenvectors are linearly independent
rank = np.linalg.matrix_rank(eigenvectors)
n = A.shape[0]

if rank == n:
    print("\n✅ The matrix is Diagonalizable.")
else:
    print("\n❌ The matrix is NOT Diagonalizable.")

# --- Step 4: Verify Cayley–Hamilton Theorem ---
# The Cayley–Hamilton theorem says: 
# Every matrix satisfies its own characteristic equation.

# Characteristic polynomial: |A - λI| = 0
# Instead of doing it manually, we can use numpy.poly
# np.poly(A) gives coefficients of characteristic polynomial
# Example: λ² - 7λ + 10 → [1, -7, 10]

coeff = np.poly(A)
print("\nCharacteristic Polynomial Coefficients:")
print(coeff)

# Now verify A² - 7A + 10I = 0 using np.poly
# (for 2×2, this is general form; works for any n×n too)

# Make an identity matrix of same size
I = np.identity(n)

# Start with a zero matrix
result = np.zeros_like(A)

# Apply the polynomial: coeff[0]*A^n + coeff[1]*A^(n-1) + ... + coeff[n]*I
# (last term is constant)
for i in range(n + 1):
    power = n - i
    term = coeff[i] * (np.linalg.matrix_power(A, power) if power > 0 else I)
    result += term

print("\nResult of substituting A into its characteristic polynomial:")
print(np.round(result, 4))

if np.allclose(result, np.zeros_like(A)):
    print("\n✅ Cayley–Hamilton Theorem is VERIFIED.")
else:
    print("\n❌ Cayley–Hamilton Theorem is NOT satisfied.")
