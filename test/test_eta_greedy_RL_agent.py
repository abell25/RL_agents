from unittest import TestCase
from pick_hole_agents.eta_greedy_RL_agent import eta_greedy_RL_agent

__author__ = 'anthony bell'


class TestEta_greedy_RL_agent(TestCase):
    def setUp(self):
        self.win_score = 1.0
        self.lose_score = 0.0

    def test_should_update_Q_correctly(self):
        agent = eta_greedy_RL_agent(4, 'rl_agent', init_Q=0.0, eta=0.1)

        agent.latest_pick = 0
        agent.win()
        agent.latest_pick = 0
        agent.win()

        agent.latest_pick = 1
        agent.win()
        agent.latest_pick = 1
        agent.lose()

        agent.latest_pick = 2
        agent.lose()


        self.assertEqual(agent.Q[0], 1.0)
        self.assertEqual(agent.Q[1], 0.5)
        self.assertEqual(agent.Q[2], 0.0)
        self.assertEqual(agent.Q[3], 0.0)

    def test_should_not_produce_samples_for_bad_action(self):
        agent = eta_greedy_RL_agent(4, 'rl_agent', init_Q=0.0, eta=0.1)
        #[1.0, 0.0, 0.0 0.0]
        agent.latest_pick = 0
        agent.win()
        self.assertEqual(agent.greedy_from_Q(range(4)), 0)

        #[0.5, 0.0, 0.0 0.0]
        agent.latest_pick = 0
        agent.lose()
        self.assertEqual(agent.greedy_from_Q(range(4)), 0)

        #[0.66, 0.0, 0.0 0.0]
        agent.latest_pick = 0
        agent.win()
        self.assertEqual(agent.greedy_from_Q(range(4)), 0)

        #[0.66, 1.0, 0.0 0.0]
        agent.latest_pick = 1
        agent.win()
        self.assertEqual(agent.greedy_from_Q(range(4)), 1)

        #[0.66, 0.5, 0.0 0.0]
        agent.latest_pick = 1
        agent.lose()
        self.assertEqual(agent.greedy_from_Q(range(4)), 0)

        #[0.66, 0.5, 0.0 0.0]
        agent.latest_pick = 2
        agent.lose()
        self.assertEqual(agent.greedy_from_Q(range(4)), 0)

        #[0.4, 0.5, 0.0 0.0]
        agent.latest_pick = 0
        agent.lose()
        agent.lose()
        self.assertEqual(agent.greedy_from_Q(range(4)), 1)



