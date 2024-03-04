import numpy as np
import matplotlib.pyplot as plt


def initial_state(grid_size):
    state = np.random.choice([-1,1], size=(grid_size, grid_size))
    return state

def hamiltonian(state, external_field, J=0.5):
    dim = np.shape(state)[0]
    neighbor_indices = [i for i in range(1,dim)] +[0]
    nearest_neighbors_x = -J * np.sum(state * state[:,neighbor_indices])
    nearest_neighbors_y = -J * np.sum(state * state[neighbor_indices,:])
    H = nearest_neighbors_x + nearest_neighbors_y
    return H 

def metropolis_hastings()
s = initial_state(3)
