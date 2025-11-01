import numpy as np

# ---------- Step 1: Create matrices ----------

# Coefficient matrix A
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])

# Constant matrix B (Right-hand side)
B = np.array([[8],
              [-11],
              [-3]])

print("Coefficient Matrix (A):", A)
print("\nConstant Matrix (B):", B)

# ---------- Step 2: Combine A and B to form augmented matrix ----------
AB = np.hstack([A, B])
print("Augmented Matrix [A|B]:", AB)

# ---------- Step 3: Perform Gauss Elimination ----------
n = len(B)

for i in range(n):
    # Make the diagonal element 1
    AB[i] = AB[i] / AB[i, i]

    # Make elements below diagonal 0
    for j in range(i + 1, n):
        AB[j] = AB[j] - AB[j, i] * AB[i]

print("Upper Triangular Form after Gauss Elimination:", np.round(AB, 2))

# ---------- Step 4: Back Substitution ----------
X = np.zeros((n, 1))

for i in range(n - 1, -1, -1):
    X[i] = AB[i, -1] - np.dot(AB[i, i + 1:n], X[i + 1:n])

print("Solution of the System (X):", X)
