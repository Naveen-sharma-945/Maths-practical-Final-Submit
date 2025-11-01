import numpy as np

# Step 1: Create a grid of x, y, z points
x = np.linspace(0, 2, 5)
y = np.linspace(0, 2, 5)
z = np.linspace(0, 2, 5)

X, Y, Z = np.meshgrid(x, y, z)

# Step 2: Define the vector field F = (Fx, Fy, Fz)
# Example: F = (y*z, x*z, x*y)
Fx = Y * Z
Fy = X * Z
Fz = X * Y

# Step 3: Compute partial derivatives using numpy.gradient
dFx_dy = np.gradient(Fx, y, axis=1)
dFx_dz = np.gradient(Fx, z, axis=2)

dFy_dx = np.gradient(Fy, x, axis=0)
dFy_dz = np.gradient(Fy, z, axis=2)

dFz_dx = np.gradient(Fz, x, axis=0)
dFz_dy = np.gradient(Fz, y, axis=1)

# Step 4: Apply curl formula
curl_x = dFz_dy - dFy_dz
curl_y = dFx_dz - dFz_dx
curl_z = dFy_dx - dFx_dy

# Step 5: Combine all components
curl = (curl_x, curl_y, curl_z)

# Step 6: Print result
print("Curl of the vector field (components):")
print("Curl_x =\n", curl_x)
print("Curl_y =\n", curl_y)
print("Curl_z =\n", curl_z)
