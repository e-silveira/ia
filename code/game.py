from enum import Enum

Player = Enum('Player', ['MAX', 'MIN'])

class Game:
    def __init__(self, initial):
        self.initial = initial
        self.to_move = Player.MAX
        pass

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def is_terminal(self, state):
        pass

    def utility(self, player):
        pass
