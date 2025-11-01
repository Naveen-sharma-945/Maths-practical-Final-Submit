
# Coefficient Matrix (A) Elements
print("Enter the Dimension of Matrix (A):")
NR = int(input("Enter the Number of Rows: "))
NC = int(input("Enter the Number of Columns: "))

print("Enter the Elements of Matrix (A) in a single line (separated by space):")
Entries = list(map(float, input().split()))
A = np.array(Entries).reshape(NR, NC)

print("Matrix (A) is as follows:", A)