import numpy as np
import matplotlib.pyplot as plt

# Rectangle dimensions and corner radius
w = 8  # Width
h = 4  # Height
r = 1  # Corner radius

# Number of points per arc
n_points = 100

# Generate the rounded corners
# Top-right corner
theta1 = np.linspace(0, np.pi/2, n_points)
x1 = w/2 - r + r * np.cos(theta1)
y1 = h/2 - r + r * np.sin(theta1)

# Top-left corner
theta2 = np.linspace(np.pi/2, np.pi, n_points)
x2 = -w/2 + r + r * np.cos(theta2)
y2 = h/2 - r + r * np.sin(theta2)

# Bottom-left corner
theta3 = np.linspace(np.pi, 3*np.pi/2, n_points)
x3 = -w/2 + r + r * np.cos(theta3)
y3 = -h/2 + r + r * np.sin(theta3)

# Bottom-right corner
theta4 = np.linspace(3*np.pi/2, 2*np.pi, n_points)
x4 = w/2 - r + r * np.cos(theta4)
y4 = -h/2 + r + r * np.sin(theta4)

# Combine all points
x = np.concatenate([x1, x2, x3, x4])
y = np.concatenate([y1, y2, y3, y4])

# Plot the rounded rectangle
plt.figure(figsize=(8, 4))
plt.plot(np.append(x, x[0]), np.append(y, y[0]), label='Rounded Rectangle', color='blue')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Rounded Rectangle")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
plt.savefig("rounded_rectangle.png")