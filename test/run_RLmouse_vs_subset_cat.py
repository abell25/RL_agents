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

if __name__ == "__main__":
    run_RLmouse_vs_subset_cat()
