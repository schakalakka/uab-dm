import random
import numpy as np
import pygal
import pickle

N_list = [150, 200, 250]  # number of people
gamma = 0.5  # healing chance
T_list = [250, 300, 350, 1000]  # number of time units computed
betas = np.concatenate((np.linspace(0, 0.31, 10), np.linspace(0.32, 0.7, 100), np.linspace(0.705, 1, 20)),
                       axis=0)  # infection rates
runs = 100  # number of repetitions for the average
