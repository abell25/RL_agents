__author__ = 'anthony bell'

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


class cat_mouse_game():
    def __init__(self, cats, mice, num_holes):
        self.cats = cats
        self.mice = mice
        self.num_holes = num_holes

        self.reset_game()

    def reset_game(self):
        self.round = 0

        for cat in self.cats:
            cat.reset()
        for mouse in self.mice:
            mouse.reset()

    def run_n_rounds(self, n):
        for k in range(n):
            self.run_single_round()

    def run_single_round(self):
        self.round += 1
        holes = np.array(range(self.num_holes))

        cats_choices = cat_mouse_game.__get_holes_picked_by_agents(self.cats, holes)
        mice_choices = cat_mouse_game.__get_holes_picked_by_agents(self.mice, holes)

        holes_with_collisions = set(cats_choices).intersection(set(mice_choices))
        cats_that_found_mouse = set()
        mice_that_were_found = set()

        for hole in holes_with_collisions:
            for cat_idx in cats_choices[hole]:
                cats_that_found_mouse.add(cat_idx)
            for mouse_idx in mice_choices[hole]:
                mice_that_were_found.add(mouse_idx)

        for i, mouse in enumerate(self.mice):
            if i in mice_that_were_found:
                mouse.lose()
            else:
                mouse.win()

        for i, cat in enumerate(self.cats):
            if i in cats_that_found_mouse:
                cat.win()
            else:
                cat.lose()


    @staticmethod
    def __get_holes_picked_by_agents(agents, holes):
        agent_choices = {}
        for i, agent in enumerate(agents):
            choice = agent.pick_hole(holes)
            if choice not in agent_choices:
                agent_choices[choice] = [i]
            else:
                agent_choices[choice].append(i)

        return agent_choices