# gradient_numpy.py
import numpy as np

def f(x, y):
    return x**2 + 3 * y**2

x = np.linspace(-2, 2, 9)
y = np.linspace(-2, 2, 9)
X, Y = np.meshgrid(x, y, indexing='xy')
F = f(X, Y)

# numpy.gradient returns gradient along each axis;
# since F is shape (rows, cols): grad_y, grad_x = np.gradient(F, dy, dx)
dx = x[1] - x[0]
dy = y[1] - y[0]

dF_dy, dF_dx = np.gradient(F, dy, dx)  # order: axis 0 (rows->y), axis 1 (cols->x)

print("Numerical dF/dx (center 3x3):\n", np.round(dF_dx[3:6, 3:6], 4))
print("Numerical dF/dy (center 3x3):\n", np.round(dF_dy[3:6, 3:6], 4))

# analytic comparison
print("\nAnalytic dF/dx (center 3x3):\n", np.round(2 * X[3:6, 3:6], 4))
print("Analytic dF/dy (center 3x3):\n", np.round(6 * Y[3:6, 3:6], 4))
