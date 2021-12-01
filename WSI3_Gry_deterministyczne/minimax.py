import numpy

import isolation_game as ig
from copy import deepcopy
import random


def bot_move(game, maximizing, max_depth, who):
    best_score = -100
    best_move = 0
    list_moves = game.get_moves()
    for move in list_moves:
        game_copy = deepcopy(game)
        game.move(move)
        score = minimax(game, 0, maximizing, max_depth, who)
        game = game_copy
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def minimax(game, depth, maximizing, max_depth, who):
    if depth == max_depth:
        return 0
    if len(game.get_moves()) == 0:
        lost = game.get_current_player()
        if who == 2:
            if lost == 1:
                return -1
            elif lost == 2:
                return 1
        if who == 1:
            if lost == 1:
                return 1
            elif lost == 2:
                return -1
    if maximizing:
        best_score = -100
        list_moves = game.get_moves()
        for move in list_moves:
            game_copy = deepcopy(game)
            game.move(move)
            score = minimax(game, depth + 1, False, max_depth, -who)
            game = game_copy
            if score > best_score:
                best_score = score
        return best_score
    else:
        best_score = 100
        list_moves = game.get_moves()
        for move in list_moves:
            game_copy = deepcopy(game)
            game.move(move)
            score = minimax(game, depth + 1, True, max_depth, -who)
            game = game_copy
            if score < best_score:
                best_score = score
        return best_score


def play_mm_v_mm():
    game = ig.Isolation(4, (1, 1), (4, 4))
    while True:
        game_copy = deepcopy(game)
        print(game)
        if len(game.get_moves()) == 0:
            if game.check_if_draw():
                print("draw")
                return 'DRAW'
            else:
                lost = game.get_current_player()
                print(f"Player {lost} lost")
                return lost
        best_move = bot_move(game_copy, False, 8, 1)
        game.move(best_move)

        game_copy = deepcopy(game)
        print(game)
        if len(game.get_moves()) == 0:
            if game.check_if_draw():
                print("draw")
                return 'DRAW'
            else:
                lost = game.get_current_player()
                print(f"Player {lost} lost")
                return lost
        best_move = bot_move(game_copy, True, 8, 2)
        game.move(best_move)


def play_mm_v_r():
    game = ig.Isolation(4, (1, 1), (4, 4))
    while True:
        print(game)
        if len(game.get_moves()) == 0:
            if game.check_if_draw():
                print("draw")
                return 'DRAW'
            else:
                lost = game.get_current_player()
                print(f"Player {lost} lost")
                return lost
        moves = game.get_moves()
        rnd_move = random.choice(moves)
        game.move(rnd_move)

        game_copy = deepcopy(game)
        print(game)
        if len(game.get_moves()) == 0:
            if game.check_if_draw():
                print("draw")
                return 'DRAW'
            else:
                lost = game.get_current_player()
                print(f"Player {lost} lost")
                return lost
        best_move = bot_move(game_copy, False, 8, 2)
        game.move(best_move)


def statistics(times):
    returns = []
    for i in range(times):
        returns.append(play_mm_v_r())
    stats = numpy.unique(returns, return_counts=True)
    return stats



# play_mm_v_mm()
# play_mm_v_r()
print(statistics(10))