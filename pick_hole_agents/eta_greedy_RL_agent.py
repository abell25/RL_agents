__author__ = 'anthony bell'

from pick_agent import pick_agent
import random
import numpy as np
from scipy.stats import rv_discrete

class eta_greedy_RL_agent(pick_agent):
    def __init__(self, num_holes, name, init_Q = 0.5, eta=0.1, step_size=None):
        self.Q = np.ones(num_holes) * init_Q
        self.action_counts = np.zeros(num_holes)
        self.action_sums = np.zeros(num_holes)

        self.eta = eta
        self.step_size = None

        pick_agent.init(self, num_holes, name)


    def pick_hole_stategy(self, holes):
        hole = self.eta_greedy(holes, self.eta)
        return hole

    def win(self):
        self.update_Q(self.latest_pick, 1.0)
        pick_agent.win_update(self)

    def lose(self):
        self.update_Q(self.latest_pick, 0.0)
        pick_agent.lose_update(self)

    def update_Q(self, a, reward):
        self.action_counts[a] += 1
        self.action_sums[a] += reward # not needed anymore since we are updating Q incrementally.
        # Q_k = Q_{k-1} + 1/k * [ r_k - Q_{k-1}] or
        # Q_k = Q_{k-1} + alpha*[ r_k - Q_{k-1}]
        step_size = self.step_size if self.step_size is not None else 1/(self.action_counts[a])
        self.Q[a] = self.Q[a] + step_size * (reward - self.Q[a])


    def eta_greedy(self, holes, eta=0.1):
        if random.random() < eta:
            return random.choice(holes)
        else:
            return self.greedy_from_Q(holes)


    def greedy_from_Q(self, holes):
        Q = self.Q[holes]

        Q_indexes = np.array(range(len(Q)))
        max_indexes = Q_indexes[Q == np.max(Q)]
        random_max_index = random.choice(max_indexes)

        #return holes[np.argmax(Q)]
        return holes[random_max_index]