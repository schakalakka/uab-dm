from config import *


def compute(N, T):
    """
    Version WITH periodic boundary condition (called circular)
    Computes for a given number of people and a number of time steps the fraction of sick people for several infection
    rates
    Additional parameters taken into account: healing chance (gamma), infection rates (betas) and runs over which the
    average is taken
    :param N: number of people
    :param T: number of time steps
    :return: list of fraction of sick people corresponding to the betas
    """
    print(N, T)
    fraction_of_sick_people = np.zeros(len(betas))
    for k, beta in enumerate(betas):
        for run in range(runs):
            # initialize random array with its state sick/healthy
            # 0 for healthy
            # 1 for infected/sick
            current_state = np.random.randint(0, 2, N)
            for j in range(T):
                next_state = np.zeros(N, dtype=int)
                for i in range(N):
                    if current_state[i] == 0:  # is healthy and cannot infect anyone
                        continue
                    if random.random() < beta:  # infect left neighbour
                        next_state[i - 1] = 1
                    if random.random() < beta:  # infect right neighbour
                        next_state[(i + 1) % N] = 1
                    # next_state[i] == 0 means current person is not yet infected by left neighbour
                    # because of if current_state[i] == 0 we know that the current person is sick
                    # with random.random() <= beta we "roll a dice" if it gets healthy
                    # if not it is going to be sick
                    # Note: In the round of i+1 it can still be infected!
                    if next_state[i] == 0 and random.random() <= gamma:
                        next_state[i] = 0
                    else:
                        next_state[i] = 1
                current_state = next_state.copy()
            fraction_of_sick_people[k] += sum(current_state) / N
        fraction_of_sick_people[k] = fraction_of_sick_people[k] / runs
    return fraction_of_sick_people


def compute_noncircular(N, T):
    """
     Version without periodic boundary condition (called non-circular)
     Computes for a given number of people and a number of time steps the fraction of sick people for several infection
     rates
     Additional parameters taken into account: healing chance (gamma), infection rates (betas) and runs over which the
     average is taken
     :param N: number of people
     :param T: number of time steps
     :return: list of fraction of sick people corresponding to the betas
     """
    print(N, T, 'non')
    fraction_of_sick_people = np.zeros(len(betas))
    for k, beta in enumerate(betas):
        for run in range(runs):
            # initialize random array with its state sick/healthy
            # 0 for healthy
            # 1 for infected/sick
            current_state = np.random.randint(0, 2, N)
            for j in range(T):
                next_state = np.zeros(N, dtype=int)
                for i in range(N):
                    if current_state[i] == 0:  # is healthy and cannot infect anyone
                        continue
                    if random.random() < beta and i > 0:  # infect left neighbour
                        next_state[i - 1] = 1
                    if random.random() < beta and i < N - 1:  # infect right neighbour
                        next_state[(i + 1) % N] = 1
                    # next_state[i] == 0 means current person is not yet infected by left neighbour
                    # because of if current_state[i] == 0 we know that the current person is sick
                    # with random.random() <= beta we "roll a dice" if it gets healthy
                    # if not it is going to be sick
                    # Note: In the round of i+1 it can still be infected!
                    if next_state[i] == 0 and random.random() <= gamma:
                        next_state[i] = 0
                    else:
                        next_state[i] = 1
                current_state = next_state.copy()
            fraction_of_sick_people[k] += sum(current_state) / N
        fraction_of_sick_people[k] = fraction_of_sick_people[k] / runs
    return fraction_of_sick_people


def compute_dataset(N, T, circular=True):
    """
    Compute dataset for specific number of people and time steps and dump/pickle it to a file
    :param N: number of people
    :param T: time steps
    :param circular: boolean, if True the begin and end of the array are neighbours
    :return:
    """
    if circular:
        data_set = compute(N, T)
        with open(f'datasets/dataset_{N}_{T}_circular.pickle', 'wb') as f:
            pickle._dump(data_set, f)
    else:
        data_set = compute_noncircular(N, T)
        with open(f'datasets/dataset_{N}_{T}_non_circular.pickle', 'wb') as f:
            pickle._dump(data_set, f)


compute_dataset(150, 250)
compute_dataset(150, 300)
compute_dataset(150, 350)
compute_dataset(150, 1000)
compute_dataset(150, 250, circular=False)
compute_dataset(150, 300, circular=False)
compute_dataset(150, 350, circular=False)
compute_dataset(150, 1000, circular=False)

compute_dataset(200, 250)
compute_dataset(200, 300)
compute_dataset(200, 350)
compute_dataset(200, 1000)
compute_dataset(200, 250, circular=False)
compute_dataset(200, 300, circular=False)
compute_dataset(200, 350, circular=False)
compute_dataset(200, 1000, circular=False)

compute_dataset(250, 250)
compute_dataset(250, 300)
compute_dataset(250, 350)
compute_dataset(250, 1000)
compute_dataset(250, 250, circular=False)
compute_dataset(250, 300, circular=False)
compute_dataset(250, 350, circular=False)
compute_dataset(250, 1000, circular=False)
