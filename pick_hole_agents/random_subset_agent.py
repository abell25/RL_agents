__author__ = 'anthony bell'

from pick_agent import pick_agent
import random

class random_subset_agent(pick_agent):
    def __init__(self, num_holes, holes_to_consider, name):
        pick_agent.init(self, num_holes, name)
        self.holes_to_consider = holes_to_consider

    def pick_hole_stategy(self, holes):
        holes_available = list(set(holes).intersection(set(self.holes_to_consider)))
        if len(holes_available) > 0:
            return random.choice(holes_available)
        else:
            #all the holes to consider are selected, so we will pick a random hole now.
            return random.choice(holes)
