# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:58:56 2026

@author: chakr
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
os.makedirs("plots", exist_ok=True)

# Parameters

N = 100
K = 1.0
dt = 0.01
noise_strength = 0.1
steps = 300

# We Initialize field
theta = np.random.rand(N, N) * 2 * np.pi

# We define the Laplacian
def laplacian(field):
    return (
        np.roll(field, 1, axis=0) +
        np.roll(field, -1, axis=0) +
        np.roll(field, 1, axis=1) +
        np.roll(field, -1, axis=1) -
        4 * field
    )

# Updating field
def update_field():
    global theta
    noise = noise_strength * np.random.randn(N, N)
    dtheta = K * laplacian(theta) + noise
    theta = theta + dt * dtheta
# Plot setup
fig, ax = plt.subplots()
im = ax.imshow(theta, cmap='hsv', vmin=0, vmax=2*np.pi,animated=True)
plt.colorbar(im)

# Animation update
def update(frame):
    update_field()
    im.set_array(theta)
    ax.set_title(f"Step {frame}")
    return [im]
ani = animation.FuncAnimation(
    fig,
    update,
    frames=steps,
    interval=50,
    blit=True
)

html_path = html_path = r"C:\Users\chakr\Desktop\field_evolution.html"
with open(html_path, "w") as f:
    f.write(ani.to_jshtml())

print(f"HTML animation saved at {html_path}")

plt.close()
