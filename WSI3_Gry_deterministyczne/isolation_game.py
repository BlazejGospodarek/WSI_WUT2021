import random
import numpy
from numpy import unique


class Isolation:
    def __init__(self, size, player_1_pos, player_2_pos):
        self._size = size
        self._player1_pos = player_1_pos
        self._player2_pos = player_2_pos
        self._clear_board = [[' ' for _x in range(size)] for _x in range(size)]
        self._board_with_players = self.set_players()
        self.player_move = 1
        self.player_wait = 2

    def __str__(self):
        board = ''
        sep = '\n' + '+---'*self._size + '+\n'
        for y in range(self._size):
            board += '|' + sep
            for x in range(self._size):
                if self._board_with_players[y][x] == "1" \
                        or self._board_with_players[y][x] == "2" \
                        or self._board_with_players[y][x] == "X":
                    board += f'| {self._board_with_players[y][x]} '
                else:
                    board += '|   '
        board += '|' + sep
        return board

    def get_current_player(self):
        return self.player_move

    def change_move(self):
        if self.player_move == 1:
            self.player_move = 2
            self.player_wait = 1
        else:
            self.player_move = 1
            self.player_wait = 2

    def get_board(self):
        return self._board_with_players

    def set_players(self):
        board = self._clear_board
        board[self._player1_pos[1] - 1][self._player1_pos[0] - 1] = '1'
        board[self._player2_pos[1] - 1][self._player2_pos[0] - 1] = '2'
        return board

    def get_moves(self):
        moves = {
            "n": (0, -1),
            "s": (0, 1),
            "w": (-1, 0),
            "e": (1, 0),
            "nw": (-1, -1),
            "ne": (1, -1),
            "sw": (-1, 1),
            "se": (1, 1)
        }
        moves_available = []
        if self.player_move == 1:
            x, y = self._player1_pos
        elif self.player_move == 2:
            x, y = self._player2_pos
        for m in moves:
            pos_change = moves[m]
            if x + pos_change[0] > self._size or x + pos_change[0] < 1 or y + pos_change[1] > self._size \
                    or y + pos_change[1] < 1:
                pass
            elif self._board_with_players[y - 1 + pos_change[1]][x - 1 + pos_change[0]] == "1"\
                    or self._board_with_players[y - 1 + pos_change[1]][x - 1 + pos_change[0]] == "2"\
                    or self._board_with_players[y - 1 + pos_change[1]][x - 1 + pos_change[0]] == "X":
                pass
            else:
                moves_available.append(m)
        return moves_available

    def check_if_draw(self):
        if len(self.get_moves()) == 0:
            self.change_move()
            if len(self.get_moves()) == 0:
                return True
            self.change_move()
        else:
            return False

    def move(self, move):
        moves = {
            "n": (0, -1),
            "s": (0, 1),
            "w": (-1, 0),
            "e": (1, 0),
            "nw": (-1, -1),
            "ne": (1, -1),
            "sw": (-1, 1),
            "se": (1, 1)
        }
        if self.player_move == 1:
            x, y = self._player1_pos
            self._player1_pos = (x + moves[str(move)][0], y + moves[str(move)][1])
        elif self.player_move == 2:
            x, y = self._player2_pos
            self._player2_pos = (x + moves[str(move)][0], y + moves[str(move)][1])
        move_board = self._board_with_players
        move_board[y-1][x-1] = 'X'
        move_board[y + moves[str(move)][1]-1][x + moves[str(move)][0]-1] = str(self.player_move)
        self._board_with_players = move_board
        self.change_move()
        return

#
# def play():
#     game = Isolation(5, (1, 1), (1, 2))
#     while True:
#         print(game)
#         if len(game.get_moves()) == 0:
#             lost = game.get_current_player()
#             print(f"Player {lost} lost")
#             return lost
#         moves_possible = game.get_moves()
#         random_move = random.choice(moves_possible)
#         game.move(random_move)
#         game.change_move()
#
#
# def get_stats(games):
#     wins = []
#     for i in range(games):
#         winner = play()
#         wins.append(winner)
#     return wins
#
#
# lsita = numpy.unique(get_stats(100), return_counts=True)
# print(lsita)
