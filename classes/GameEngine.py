import numpy as np

from classes.Board import Board
from classes.Brick import Brick
from const.const_bricks import *


class GameEngine:

    def __init__(self):
        self._board = Board()
        self._candidate_bricks = \
            [
                line_type,
                four_z_type,
                four_l_type,
                t_type,
                bridge_type,
                equal_l_type,
                five_l_type,
                five_equal_z_type,
                five_unequal_z_type,
                two_square_type
            ]
        self._combinations = []

    @property
    def candidate_bricks(self):
        return self._candidate_bricks

    @property
    def board(self):
        return self._board

    def start_game(self):
        month = input("Month: ")
        day = input("Day: ")
        day_of_the_week = input("Day of the week: ")
        self._board.set_day(month, day, day_of_the_week)
        self.get_all_combinations()
        self.search(self._combinations, 0)
        self._board.display()

    def get_all_combinations(self):
        for type_idx in range(len(self._candidate_bricks)):
            type_placements = []
            for brick_idx in range(len(self._candidate_bricks[type_idx])):
                for x in range(self._board.rows):
                    for y in range(self._board.cols):
                        if self._board.put_brick(x, y, self._candidate_bricks[type_idx][brick_idx]):
                            if not self.prune():
                                type_placements.append((x, y, brick_idx, type_idx))
                            self._board.remove_brick(x, y, self._candidate_bricks[type_idx][brick_idx])
            self._combinations.append(type_placements)

    def search(self, selectable_types, layer):
        if layer == 10:
            return True

        bricks = selectable_types[layer]
        for x, y, brick_idx, type_idx in bricks:
            if self._board.put_brick(x, y, self._candidate_bricks[type_idx][brick_idx]):
                # if layer < 5:
                #     print(" " * layer + "{}".format(layer))
                # self._board.display()
                if not self.prune() and self.search(selectable_types, layer+1):
                    return True
                self._board.remove_brick(x, y, self._candidate_bricks[type_idx][brick_idx])

        return False

    def prune(self):
        embedded_board_array = np.ones((self._board.rows + 2, self._board.cols + 2))
        embedded_board_array[1: 1 + self._board.rows, 1: 1 + self._board.cols] = self._board.transform_to_array()

        hole_cases = [(1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 2)]
        for row, col in hole_cases:
            for i in range(self._board.rows - row + 1):
                for j in range(self._board.cols - col + 1):
                    if np.sum(embedded_board_array[1 + i: 1 + i + row, 1 + j: 1 + j + col]) < (row * col):
                        wall = np.sum(embedded_board_array[i: 1 + i + row + 1, j: 1 + j + col + 1]) - \
                               np.sum(embedded_board_array[1 + i: 1 + i + row, 1 + j: 1 + j + col]) - \
                               embedded_board_array[i, j] - \
                               embedded_board_array[i, 1 + j + col] - \
                               embedded_board_array[1 + i + row, j] - \
                               embedded_board_array[1 + i + row, 1 + j + col]
                        if wall > (2 * (row + col) - 1):
                            return True
        return False

    def clear_board(self):
        self._board = Board()


if __name__ == "__main__":
    game = GameEngine()
    game.start_game()
