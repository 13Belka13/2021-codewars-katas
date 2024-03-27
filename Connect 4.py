import numpy as np
class Connect4():

    def __init__(self):
        self.game_map = [[0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0]]
        self.game_over = False
        self.turn = 1


    def check_game_status(self):
        for col in self.game_map:
            if '1111' in ''.join(map(str, col)) or '2222' in ''.join(map(str, col)):
                self.game_over = True
                return "Player " + str(self.turn) + " wins!"

        for col in zip(*self.game_map):
            if '1111' in ''.join(map(str, col)) or '2222' in ''.join(map(str, col)):
                self.game_over = True
                return "Player " + str(self.turn) + " wins!"

        for i in range(-3, 3):
            if '1111' in ''.join(map(str, np.fliplr(np.array(self.game_map)).diagonal(i))) or '2222' in ''.join(map(str, np.fliplr(np.array(self.game_map)).diagonal(i))) \
                    or '1111' in ''.join(map(str, np.diagonal(np.array(self.game_map), i))) or '2222' in ''.join(map(str, np.diagonal(np.array(self.game_map), i))):
                self.game_over = True
                return "Player " + str(self.turn) + " wins!"



    def play(self, col):
        if self.game_over: return "Game has finished!"
        elif self.game_map[col][0] == 0:
            self.game_map[col][''.join(list(map(str, self.game_map[col]))).rindex('0')] = self.turn
            self.check_game_status()
            if self.game_over == True:
                return self.check_game_status()
            if self.turn == 1:
                self.turn = 2
                return "Player 1 has a turn"
            else:
                self.turn = 1
                return "Player 2 has a turn"
        else: return "Column full!"


c = Connect4()
print(c.play(0))
c.play(1)
c.play(0)
c.play(1)
c.play(0)
c.play(1)
print(c.play(0))