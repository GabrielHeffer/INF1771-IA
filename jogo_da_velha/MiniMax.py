import numpy as np
from random import random
import time


class HashGame:
    def __init__(self):
        self.hash_table = np.array([
                                    [0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]
                                    ])
        self.move_coord = (0, 0)
        return

    def assert_winner(self):
        horizontal_sum = np.sum(self.hash_table, axis=0)
        vertical_sum = np.sum(self.hash_table, axis=1)
        dig1 = self.hash_table[0, 0] + self.hash_table[1, 1] + self.hash_table[2, 2]
        dig2 = self.hash_table[0, 2] + self.hash_table[1, 1] + self.hash_table[2, 0]
        if -3 in horizontal_sum or -3 in vertical_sum or -3 in [dig1, dig2]:
            return -1
        elif 3 in horizontal_sum or 3 in vertical_sum or 3 in [dig1, dig2]:
            return 1
        if 0 not in self.hash_table:
            return 0
        return

    def avaliation(self):
        winner = self.assert_winner()
        if winner is not None:
            return winner
        value = 0
        if -1 in self.hash_table[0, :]:
            value -= 1
        if 1 in self.hash_table[0, :]:
            value += 1
        if -1 in self.hash_table[1, :]:
            value -= 1
        if 1 in self.hash_table[1, :]:
            value += 1
        if -1 in self.hash_table[2, :]:
            value -= 1
        if 1 in self.hash_table[2, :]:
            value += 1
        if -1 in self.hash_table[:, 0]:
            value -= 1
        if 1 in self.hash_table[:, 0]:
            value += 1
        if -1 in self.hash_table[:, 1]:
            value -= 1
        if 1 in self.hash_table[:, 1]:
            value += 1
        if -1 in self.hash_table[:, 2]:
            value -= 1
        if 1 in self.hash_table[:, 2]:
            value += 1
        if -1 in [self.hash_table[0, 0], self.hash_table[1, 1], self. hash_table[2, 2]]:
            value -= 1
        if 1 in [self.hash_table[0, 0], self.hash_table[1, 1], self.hash_table[2, 2]]:
            value += 1
        if -1 in [self.hash_table[0, 2], self.hash_table[1, 1], self.hash_table[2, 0]]:
            value -= 1
        if 1 in [self.hash_table[0, 2], self.hash_table[1, 1], self.hash_table[2, 0]]:
            value += 1
        return value

    def min(self):
        winner = self.assert_winner()
        if winner is not None:
            return winner
        available_houses = np.where(self.hash_table == 0)
        result = []
        for house in list(zip(available_houses[0], available_houses[1])):
            self.hash_table[house[0], house[1]] = -1
            result.append(self.avaliation())
            self.hash_table[house[0], house[1]] = 0
        return min(result)

    def max(self):
        available_houses = np.where(self.hash_table == 0)
        available_houses = list(zip(available_houses[0], available_houses[1]))
        result = []
        for house in available_houses:
            self.hash_table[house[0], house[1]] = 1
            result.append(self.min())
            self.hash_table[house[0], house[1]] = 0
        self.move_coord = available_houses[result.index(max(result))]
        return

    def minmax_decision_move(self):
        self.max()
        self.hash_table[self.move_coord[0], self.move_coord[1]] = 1
        return

    def show_hash_table(self):
        for row in range(self.hash_table.shape[0]):
            print("|", end="")
            for column in range(self.hash_table.shape[1]):
                if self.hash_table[row, column] == 1:
                    print(" X ", end="|")
                elif self.hash_table[row, column] == -1:
                    print(" O ", end="|")
                else:
                    print("   ", end="|")
            print()
        return

    def end_game(self):
        winner = self.assert_winner()
        if winner == 0:
            print("Empate!")
            return True
        elif winner == 1:
            print("Você perdeu!")
            return True
        elif winner == -1:
            print("parabéns você ganhou!")
            return True
        return False

    def play(self):
        if random() < 0.5:
            self._mode2()
        else:
            self._mode1()
        return

    def _player_turn(self):
        row = None
        column = None
        print("Sua vez")
        while row is None and column is None:
            row = int(input("linha: "))
            column = int(input("coluna: "))
            if not self.hash_table[row, column]:
                self.hash_table[row, column] = -1
            else:
                print("coordenadas invalidas")
                row = column = None
        return

    def _mode1(self):
        self.show_hash_table()
        print("Primeiro jogador IA")
        while True:
            print("Vez da IA")
            self.minmax_decision_move()
            time.sleep(2)
            self.show_hash_table()
            if self.end_game():
                break
            self._player_turn()
            self.show_hash_table()
            if self.end_game():
                break
        return

    def _mode2(self):
        self.show_hash_table()
        print("Primeiro jogador você")
        while True:
            self._player_turn()
            self.show_hash_table()
            if self.end_game():
                break
            print("Vez da IA")
            self.minmax_decision_move()
            time.sleep(2)
            self.show_hash_table()
            if self.end_game():
                break
        return



if __name__ == "__main__":
    game = HashGame()
    game.play()



