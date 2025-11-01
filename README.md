# Maths-practical-Final-Submit
<!-- 🧮 Maths Practical README.md -->

<h1 align="center">🧠 Maths Practical - Solving Matrix Problems using NumPy (Python)</h1>


<p align="center">
![Ramanujan Logo](![Logo_RCDU](https://github.com/user-attachments/assets/c52c30a7-4831-4c40-a6a4-d2c722e0ab5c)
)

</p>

<h3 align="center">📘 Department of Computer Science</h3>
<h3 align="center">Ramanujan College, University of Delhi</h3>

---

### 🧾 Project Overview

This project demonstrates how to **solve matrix-related problems** using **NumPy** in Python.  
It includes examples such as:

- Finding **determinant** of a matrix  
- Checking **singular/non-singular** property  
- Finding **inverse** of a matrix  
- Computing **eigenvalues and eigenvectors**  
- Performing **matrix multiplication, addition, and transpose**

---

### 💻 Technology Used

- **Language:** Python 🐍  
- **Library:** NumPy 🔢  
- **Platform:** Jupyter Notebook / VS Code  

---

### 🧮 Sample Output

```python
import numpy as np

A = np.array([[2, 3], [1, 4]])
det = np.linalg.det(A)
print("Determinant:", det)
