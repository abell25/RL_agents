__author__ = 'anthony bell'

from cat_mouse_game import cat_mouse_game
from pick_strategy import pick_strategy

def run_RLmouse_vs_subset_cat():
    num_holes = 8
    cats = [pick_strategy.random_subset_agent(num_holes, [0], 'cat_0'),
            pick_strategy.random_subset_agent(num_holes, [0, 1], 'cat_1')]
    mice = [pick_strategy.eta_greedy_RL_agent(num_holes, 'mouse_0', init_Q=0.0, eta=0.1)]
    game = cat_mouse_game(cats, mice, num_holes)

    game.reset_game()
    num_rounds = 50

    for k in range(1, 51):
        game.run_n_rounds(num_rounds)
        mouse_dist = mice[0].get_str_hole_distribution()
        cat_dist = cats[0].get_str_hole_distribution()

        print("{0:04d}: mouse: {1}, cat: {2}".format(game.round, mouse_dist, cat_dist))


def run_RLmouse_vs_sequence_cat():
    num_holes = 5
    cats = [pick_strategy.sequence_agent(num_holes, [[0], [1], [2], [3], [4]], [500, 500, 500, 500, 500], 'cat_0')]
    #mice = [pick_strategy.eta_greedy_RL_agent(num_holes, 'mouse_0', init_Q=1.0, eta=0.1)]
    mice = [pick_strategy.softmax_RL_agent(num_holes, 'mouse_0', init_Q=1.0, temp=0.1, step_size=0.01)]
    game = cat_mouse_game(cats, mice, num_holes)

    game.reset_game()
    num_rounds = 50

    for k in range(1, 101):
        game.run_n_rounds(num_rounds)

        mouse_dist = mice[0].get_str_hole_distribution()
        cat_dist = cats[0].get_str_hole_distribution()

        mouse_last = mice[0].get_last_n_dist(50)
        cat_last = cats[0].get_last_n_dist(50)

        print("{0:04d}: mouse: {1}, cat: {2}".format(game.round, mouse_last, cat_last))




if __name__ == "__main__":
    run_RLmouse_vs_sequence_cat()
