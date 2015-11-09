
from pick_agent import pick_agent
import random

class sequence_agent(pick_agent):
    def __init__(self, num_holes, holes_to_consider, time_to_consider, name):
        pick_agent.init(self, num_holes, name)
        self.holes_to_consider = holes_to_consider
        self.time_to_consider = time_to_consider
        self.steps = zip(time_to_consider, holes_to_consider)
        self.rounds = 0
        self.step_count = 0
        self.current_step = 0

    def reset(self):
        self.rounds = 0
        self.step_count = 0
        self.current_step = 0
        pick_agent.reset(self)

    def pick_hole_stategy(self, holes):
        time_for_step, holes_for_step = self.steps[self.current_step]

        if self.step_count >= time_for_step:
            self.step_count = 0
            self.current_step = (self.current_step + 1) % len(self.steps)
            time_for_step, holes_for_step = self.steps[self.current_step]

        self.step_count += 1
        self.rounds += 1

        hole = self.pick_hole_available_in_current_step(holes, holes_for_step)
        return hole

    def pick_hole_available_in_current_step(self, holes, holes_for_step):
        holes_available = list(set(holes).intersection(set(holes_for_step)))
        if len(holes_available) > 0:
            return random.choice(holes_available)
        else:
            #all the holes to consider are selected, so we will pick a random hole now.
            return random.choice(holes)
