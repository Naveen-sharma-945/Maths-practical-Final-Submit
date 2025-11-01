import numpy as np

# Step 1: Create a grid of x, y, z points
x = np.linspace(0, 2, 5)   # 5 points from 0 to 2
y = np.linspace(0, 2, 5)
z = np.linspace(0, 2, 5)

X, Y, Z = np.meshgrid(x, y, z)

# Step 2: Define the vector field components Fx, Fy, Fz
# Example: F = (x^2, y^2, z^2)
Fx = X**2
Fy = Y**2
Fz = Z**2

# Step 3: Compute partial derivatives using numpy.gradient
dFx_dx = np.gradient(Fx, x, axis=0)
dFy_dy = np.gradient(Fy, y, axis=1)
dFz_dz = np.gradient(Fz, z, axis=2)

# Step 4: Compute divergence = sum of partial derivatives
divergence = dFx_dx + dFy_dy + dFz_dz

# Step 5: Print result
print("Divergence of the vector field:\n", divergence)
