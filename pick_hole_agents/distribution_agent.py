from pick_agent import pick_agent

import random
import numpy as np
from scipy.stats import rv_discrete

class distribution_agent(pick_agent):
    def __init__(self, num_holes, holes_distribution, name):
        pick_agent.init(self, num_holes, name)

        self.num_holes = num_holes
        self.holes_distribution = np.array(holes_distribution)

    def pick_hole_stategy(self, holes):
        probs = self.holes_distribution[holes]

        if np.sum(probs) < 1e-10:
            return random.choice(holes)

        probs = probs / float(np.sum(probs))

        dist = rv_discrete(values=(holes, probs))
        hole =  dist.rvs()
        return hole

