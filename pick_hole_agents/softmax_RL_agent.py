__author__ = 'anthony bell'

from pick_agent import pick_agent
import random
import numpy as np
from scipy.stats import rv_discrete

class softmax_RL_agent(pick_agent):
    def __init__(self, num_holes, name, init_Q = 0.5, temp=5.0):
        self.Q = np.ones(num_holes) * init_Q
        self.action_counts = np.zeros(num_holes)
        self.action_sums = np.zeros(num_holes)

        self.temp = temp

        pick_agent.init(self, num_holes, name)

    def pick_hole_stategy(self, holes):
        return self.sample_softmax(holes, self.temp)

    def sample_softmax(self, holes, temp=5.0):
        Q = self.Q[holes]
        probs = np.exp(Q/temp) / np.sum(np.exp(Q/temp))

        dist = rv_discrete(values=(range(len(probs)), probs))
        val =  dist.rvs()
        return val

    def win(self):
        self.update_Q(self.latest_pick, 1.0)
        pick_agent.win_update(self)

    def lose(self):
        self.update_Q(self.latest_pick, 0.0)
        pick_agent.lose_update(self)

    def update_Q(self, a, reward):
        self.action_counts[a] += 1
        self.action_sums[a] += reward # not needed anymore since we are updating Q incrementally.
        # Q_k = Q_{k-1} + 1/k*[ r_k - Q_{k-1}]
        self.Q[a] = self.Q[a] + 1/(self.action_counts[a]) * (reward - self.Q[a])

    def __sample_prob_avg_from_Q(self, holes):
        Q = self.Q[holes]
        if np.min(Q) < 0:
            Q = Q - np.min(Q)

        if np.sum(Q) < 1e-6:
            return random.choice(holes)

        probs = Q / float(np.sum(Q))

        dist = rv_discrete(values=(range(len(probs)), probs))
        val =  dist.rvs()
        return val