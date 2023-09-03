import numpy as np
import matplotlib.pyplot as plt


def run_sim(s0, mu, sigma, time, n_steps, n_simulations):
    # calculate time steps (time divided by number of steps)
    dt = time / n_steps
    # generate random numbers for each time step and simulation
    random_numbers = np.random.normal(size=(n_steps, n_simulations))
    # calculate the drift and diffusion components
    drift = (mu - 0.5 * sigma**2) * dt  # average change expected
    diffusion = sigma * np.sqrt(dt) * random_numbers

    # initialise array to store simulated asset prices
    asset_paths = np.zeros((n_steps + 1, n_simulations))
    asset_paths[0] = s0
    # generate asset price paths
    for x in range(1, n_steps + 1):
        asset_paths[x] = asset_paths[x - 1] * np.exp(drift + diffusion[x - 1])

    return asset_paths
