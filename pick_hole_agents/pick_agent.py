__author__ = 'anthony bell'

from abc import ABCMeta, abstractmethod
import numpy as np
import random

import logging
log = logging.getLogger(__name__)

class pick_agent():
    __metaclass__ = ABCMeta
    agent_id_count = 0

    def init(self, num_holes, name):
        self.num_holes = num_holes
        self.reset()

        if name is not None:
            self.name = name
        else:
            global agent_id_count
            self.name = "agent_" + str(agent_id_count)
            agent_id_count+=1

    def reset(self):
        self.num_rounds = 0
        self.hole_choices = np.zeros(self.num_holes)
        self.all_choices = []
        self.results = []
        self.latest_pick = None


    def get_hole_distribution(self):
        if self.num_rounds > 0:
            return self.hole_choices / float(self.num_rounds)
        else:
            return self.hole_choices

    def get_str_hole_distribution(self):
        dist = self.get_hole_distribution()
        return '[{0}]'.format(' '.join(['{0:.2f}'.format(i) for i in dist]))

    @abstractmethod
    def pick_hole_stategy(self, holes):
        """ Picks a hole from the list of available holes.

        :param holes: list of indexes available to select.
        :return: the selected value
        """
        pass

    def win(self):
        self.win_update()

    def lose(self):
        self.lose_update()

    def pick_hole(self, holes):
        hole = self.pick_hole_stategy(holes)
        self.latest_pick = hole
        log.debug("round {0}: agent {1} is picking hole {2}.\tdist: {3}".format(self.num_rounds, self.name, hole, self.get_str_hole_distribution()))
        # Record these statistics for each agent, so we can see what the probability distribution is.
        self.num_rounds += 1
        self.hole_choices[hole] += 1
        self.all_choices.append(hole)

        return hole

    def win_update(self):
        self.results.append(1.0)

    def lose_update(self):
        self.results.append(0.0)

    def summary(self, last_n=50):
        return '{0:05d}: agent: {1}\tscore: {2:.2f}/{3:.2f}\tdist:{4}'.format(self.num_rounds, self.name,
                np.mean(self.results), self.get_last_n_score(last_n),
                self.get_last_n_dist(last_n))

    def get_last_n_score(self, n):
        return np.mean(self.results[-n:])

    def get_last_n_dist(self, n):
        return getCounts(self.all_choices[-n:], range(self.num_holes))

def getCounts(arr, values):
    d = {k:0 for k in values}
    for x in arr:
        d[x] += 1

    tuples = sorted([(k, d[k]) for k in d], key=lambda x: x[0])
    return [x[1] for x in tuples]