__author__ = 'anthony bell'

from pick_hole_agents.pick_agent import pick_agent
from pick_hole_agents.random_agent import random_agent
from pick_hole_agents.random_subset_agent import random_subset_agent
from pick_hole_agents.sequence_agent import sequence_agent

from pick_hole_agents.eta_greedy_RL_agent import eta_greedy_RL_agent
from pick_hole_agents.softmax_RL_agent import softmax_RL_agent


class pick_strategy():
    @staticmethod
    def random_agent(num_holes, name):
        return random_agent(num_holes, name)

    @staticmethod
    def random_subset_agent(num_holes, holes_to_consider, name):
        return random_subset_agent(num_holes, holes_to_consider, name)

    @staticmethod
    def eta_greedy_RL_agent(num_holes, name, init_Q, eta, step_size=None):
        return eta_greedy_RL_agent(num_holes, name, init_Q, eta, step_size)

    @staticmethod
    def softmax_RL_agent(num_holes, name, init_Q, temp, step_size=None):
        return softmax_RL_agent(num_holes, name, init_Q, temp, step_size)

    @staticmethod
    def sequence_agent(num_holes, holes_to_consider, time_to_consider, name):
        return sequence_agent(num_holes, holes_to_consider, time_to_consider, name)