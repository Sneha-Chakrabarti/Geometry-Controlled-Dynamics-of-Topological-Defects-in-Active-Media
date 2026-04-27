import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
N = 100
L = 10.0
v0 = 2.0
dt = 0.01
Dr = 0.1
noise = 0.1
steps = 300

# Initializing

positions = np.random.rand(N, 2) * L
theta = np.random.rand(N) * 2 * np.pi

# Plot setup

fig, ax = plt.subplots()
scat = ax.scatter([], [])
ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_title("Active Particles")

# Update function

def update(frame):
    global positions, theta

    # orientation update
    theta += np.sqrt(2 * Dr * dt) * np.random.randn(N)

    # directions
    directions = np.column_stack((np.cos(theta), np.sin(theta)))

    # position update
    positions += v0 * directions * dt
    positions += noise * np.sqrt(dt) * np.random.randn(N, 2)

    # periodic boundaries
    positions %= L

    scat.set_offsets(positions)
    ax.set_title(f"Step {frame}")
    return scat,

# Animation

ani = animation.FuncAnimation(fig, update, frames=steps, interval=50)
html_path = r"C:\Users\chakr\Desktop\particles.html"

with open(html_path, "w") as f:
    f.write(ani.to_jshtml())

print(f"Saved at {html_path}")

plt.show()
