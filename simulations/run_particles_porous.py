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

# obstacle parameters
num_obs = 15
obs_radius = 0.6

# Initializing particles

positions = np.random.rand(N, 2) * L
theta = np.random.rand(N) * 2 * np.pi


# Initializing obstacles

obstacles = np.random.rand(num_obs, 2) * L

# Plot setup

fig, ax = plt.subplots()
scat = ax.scatter([], [], s=10)

ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_title("Active Particles in Porous Media")

# draw obstacles
for obs in obstacles:
    circle = plt.Circle(obs, obs_radius, color='black')
    ax.add_patch(circle)


# Update function

def update(frame):
    global positions, theta

    # orientation update
    theta += np.sqrt(2 * Dr * dt) * np.random.randn(N)

    # direction vectors
    directions = np.column_stack((np.cos(theta), np.sin(theta)))

    # proposed move
    new_positions = positions + v0 * directions * dt
    new_positions += noise * np.sqrt(dt) * np.random.randn(N, 2)

    
    # Collision with obstacles
    
    for i in range(N):
        for obs in obstacles:
            dist = np.linalg.norm(new_positions[i] - obs)
            if dist < obs_radius:
                # reject move (simple reflection)
                new_positions[i] = positions[i]

                # random reorientation
                theta[i] += np.pi/2 * (np.random.rand() - 0.5)

    # periodic boundaries
    new_positions %= L

    positions[:] = new_positions

    scat.set_offsets(positions)
    ax.set_title(f"Step {frame}")

    return scat,
  
# Animation

ani = animation.FuncAnimation(fig, update, frames=steps, interval=50)

html_path = r"C:\Users\chakr\Desktop\porous_particles.html"

with open(html_path, "w") as f:
    f.write(ani.to_jshtml())

print(f"Saved at {html_path}")

plt.show()
