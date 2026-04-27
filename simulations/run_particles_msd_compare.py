import numpy as np
import matplotlib.pyplot as plt

# Parameters

N = 100
L = 10.0
v0 = 2.0
dt = 0.01
Dr = 0.1
noise = 0.1
steps = 800

obs_list = [0, 10, 20, 40]   # different obstacle densities
obs_radius = 0.6

# Function to simulate + compute MSD

def simulate_msd(num_obs):

    positions = np.random.rand(N, 2) * L
    theta = np.random.rand(N) * 2 * np.pi
    obstacles = np.random.rand(num_obs, 2) * L

    traj = np.zeros((steps, N, 2))

    for t in range(steps):

        # orientation update
        theta += np.sqrt(2 * Dr * dt) * np.random.randn(N)

        directions = np.column_stack((np.cos(theta), np.sin(theta)))

        new_positions = positions + v0 * directions * dt
        new_positions += noise * np.sqrt(dt) * np.random.randn(N, 2)

        # obstacle collisions
        for i in range(N):
            for obs in obstacles:
                if np.linalg.norm(new_positions[i] - obs) < obs_radius:
                    new_positions[i] = positions[i]
                    theta[i] += np.pi/2 * (np.random.rand() - 0.5)

        new_positions %= L
        positions = new_positions

        traj[t] = positions

    # compute MSD
    msd = np.zeros(steps)
    for t in range(steps):
        disp = traj[t] - traj[0]
        msd[t] = np.mean(np.sum(disp**2, axis=1))

    return msd

# Run for different obstacle densities

time = np.arange(steps) * dt

for num_obs in obs_list:
    print(f"Running for num_obs = {num_obs}")
    msd = simulate_msd(num_obs)

    plt.plot(time, msd, label=f"obs = {num_obs}")


# Plot
plt.xlabel("Time")
plt.ylabel("MSD")
plt.title("MSD vs Time for Different Obstacle Densities")
plt.legend()
plt.grid()

plt.show()
