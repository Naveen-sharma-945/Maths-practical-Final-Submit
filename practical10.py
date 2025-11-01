# Program: Coding and Decoding a message using Non-singular Matrix
# Author: Your Name
# Concept: Application of Linear Algebra

import numpy as np

# --- Step 1: Prepare the message ---
message = "LINEAR ALGEBRA IS FUN"
print("Original message:", message)

# Convert message to uppercase and remove spaces
message = message.replace(" ", "").upper()

# --- Step 2: Convert each letter to a number (A=1, B=2, ..., Z=26) ---
numbers = [ord(ch) - 64 for ch in message]
print("\nNumeric form of message:")
print(numbers)

# --- Step 3: Choose a non-singular (invertible) matrix as key ---
# Example 3x3 matrix
key_matrix = np.array([[2, 3, 1],
                       [1, 1, 1],
                       [1, 2, 2]])

# Check if key matrix is invertible
det = np.linalg.det(key_matrix)
if det == 0:
    raise ValueError("Matrix is singular! Choose a different key matrix.")

print("\nKey (Coding) Matrix:\n", key_matrix)

# --- Step 4: Divide message numbers into groups of 3 ---
while len(numbers) % 3 != 0:
    numbers.append(0)  # padding with 0 if not multiple of 3

groups = [numbers[i:i+3] for i in range(0, len(numbers), 3)]

# --- Step 5: Encode (multiply each group by key matrix) ---
encoded_groups = [np.dot(key_matrix, group) for group in groups]
encoded = np.concatenate(encoded_groups)
print("\nEncoded numeric message:")
print(encoded)

# --- Step 6: Decode (multiply each group by inverse matrix) ---
inv_key = np.linalg.inv(key_matrix)
decoded_groups = [np.dot(inv_key, group) for group in encoded_groups]
decoded_numbers = np.round(np.concatenate(decoded_groups)).astype(int)

print("\nDecoded numeric message:")
print(decoded_numbers)

# --- Step 7: Convert back to letters ---
decoded_message = ''.join([chr(num + 64) if 1 <= num <= 26 else ' ' for num in decoded_numbers])

print("\nDecoded text message:")
print(decoded_message)
