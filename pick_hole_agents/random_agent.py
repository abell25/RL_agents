__author__ = 'anthony bell'

from pick_agent import pick_agent
import random

class random_agent(pick_agent):
    def __init__(self, num_holes, name):
        pick_agent.init(self, num_holes, name)

    def pick_hole_stategy(self, holes):
        return random.choice(holes)
