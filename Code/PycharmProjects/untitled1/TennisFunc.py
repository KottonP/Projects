from simple_markov_chain_lib import markov_chain


def TennisWinProb(p: float, n: int) -> float:  # Function to compute probability of PlayerA winning, given
    # probability of point p and number of samples n.
    markov_table = {
        '0-0': {'15-0': p, '0-15': 1 - p},  # 1st row of the pic

        '15-0': {'30-0': p, '15-15': 1 - p}, '0-15': {'15-15': p, '0-30': 1 - p},  # 2nd row

        '30-0': {'40-0': p, '30-15': 1 - p}, '15-15': {'30-15': p, '15-30': 1 - p},  # 3rd row
        '0-30': {'15-30': p, '0-40': 1 - p},

        '40-0': {'GameA': p, '40-15': 1 - p}, '30-15': {'40-15': p, 'Deuce': 1 - p},  # 4th row
        '15-30': {'Deuce': p, '15-40': 1 - p}, '0-40': {'15-40': p, 'GameB': 1 - p},

        '40-15': {'GameA': p, 'AdvA': 1 - p}, 'Deuce': {'AdvA': p, 'AdvB': 1 - p}, '15-40': {'AdvB': p, 'GameB': 1 - p},
        # 5th row

        'GameA': {'GameA': 1.}, 'AdvA': {'GameA': p, 'Deuce': 1 - p},  # 6th row
        'AdvB': {'Deuce': p, 'GameB': 1 - p}, 'GameB': {'GameB': 1.}
    }

    initial_dist = {'0-0': 1.}  # Every game starts from 0-0

    # Markov Chain construction
    mc = markov_chain(markov_table, initial_dist)
    counter = 0

    # Simulation
    for i in range(n):
        mc.start()  # new experiment
        while True:
            mc.move()
            if mc.running_state == 'GameA':
                counter += 1
                break
            elif mc.running_state == 'GameB':
                break

    phat: float = counter / n

    return phat
