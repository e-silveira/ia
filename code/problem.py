from abc import ABC, abstractmethod
from typing import Any

class Problem(ABC):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    @abstractmethod
    def actions(self, state) -> list[Any]:
        pass

    @abstractmethod
    def action_cost(self, action) -> int:
        pass

    @abstractmethod
    def result(self, action):
        pass

    @abstractmethod
    def is_goal(self, state):
        pass
