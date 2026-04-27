# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:47:12 2026

@author: chakr
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters

N = 100              # grid size
K = 1.0              # elastic constant
dt = 0.01            # time step
steps = 500          # number of iterations
noise_strength = 0.1

# Initialize field

theta = np.random.rand(N, N) * 2 * np.pi

# Laplacian (finite difference)

def laplacian(field):
    return (
        np.roll(field, 1, axis=0) +
        np.roll(field, -1, axis=0) +
        np.roll(field, 1, axis=1) +
        np.roll(field, -1, axis=1) -
        4 * field
    )

# Time evolution

def update(theta):
    noise = noise_strength * np.random.randn(N, N)
    dtheta = K * laplacian(theta) + noise
    return theta + dt * dtheta

# Simulation loop

for step in range(steps):
    theta = update(theta)

    if step % 100 == 0:
        plt.clf()
        plt.imshow(theta, cmap='hsv')
        plt.colorbar()
        plt.title(f"Step {step}")
        plt.pause(0.01)

plt.show()
