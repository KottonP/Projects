import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
from simple_markov_chain_lib import markov_chain  # import markov chain simulator


def mc_est(n: int) -> float:

    markov_table = {   # Transition Table
        0: {1: .5, 2: .5},  # from state 0 we move to state 1 with prob 0.5 and to state 2 with 0.5
        1: {0: 1/3, 3: 2/3},
        2: {2: 1.},
        3: {0: .5, 3: .25, 4: .25},
        4: {4: 1.}
    }

    # Initial Distribution
    init_dist = {0: 1.}  # we start from state 0 with probability 1

    mc = markov_chain(markov_table, init_dist)

    sample_size = n  # Ν
    running_total = 0

    for i in range(sample_size):
        mc.start()
        while mc.running_state != 2 and mc.running_state != 4:
            mc.move()
        running_total += mc.steps  # steps it took to be absorbed

    mc_estimate = running_total / sample_size
    return mc_estimate


samplesizes = 2 ** np.arange(5, 13)  # Vector with the sample sizes (N) of our experiment
M = np.arange(31)                    # Statistic samples for each N
Var = []                             # List of Var(En)

for n in samplesizes:
    En = []                          # List of the Monte Carlo estimates (En)
    for m in M:
        En.append(mc_est(n))
    Var.append(stat.variance(En))

Var = np.array(Var)
p = np.polyfit(np.log2(samplesizes), np.log2(Var), 1)       # Linear fit

plt.figure(figsize=(12, 7))  # define figure size

# Right Axes
plt.subplot(1, 2, 1)
plt.plot(samplesizes, Var)
plt.xlabel('Sample Size')
plt.ylabel('Variance')
plt.title('Linear Axis')
plt.grid(True)  # add grid-lines

# Left Axes
plt.subplot(1, 2, 2)
plt.loglog(samplesizes, Var, basex=2, basey=2)
plt.xlabel('Sample Size')
plt.ylabel('Variance')
plt.title('Log-log Axis (Slope={:.2})'.format(p[0]))
plt.grid(True)

plt.subplots_adjust(wspace=0.5)  # specify the width space
plt.show()


