from problem import Problem
from best_first import best_first
from help import print_solution
from node import print_tree

class E6(Problem):
    def actions(self, state):
        actions = {
            "a": [("b", 7), ("c", 9), ("d", 3)],
            "b": [("a", 7), ("f", 1), ("i", 4)],
            "c": [("a", 9), ("j", 5)],
            "d": [("a", 3), ("e", 1)],
            "e": [("d", 1)],
            "f": [("b", 3), ("g", 2)],
            "g": [("f", 2), ("h", 3)],
            "h": [("g", 3)],
            "i": [("b", 4), ("k", 5)],
            "j": [("c", 5), ("l", 6)],
            "k": [("i", 5), ("l", 4)],
            "l": [("j", 6), ("k", 4)]
        }

        return actions[state]

    def action_cost(self, action):
        (_, cost) = action
        return cost

    def result(self, action):
        (state, _) = action
        return state

    def is_goal(self, state):
        return state == self.goal

def heuristic(node):
    heuristic = {
        "a": 15,
        "b": 7, 
        "c": 6,
        "d": 14,
        "e": 15,
        "f": 7,
        "g": 8,
        "h": 5,
        "i": 5,
        "j": 3,
        "k": 0,
        "l": 4
    }

    return heuristic[node.state]

if __name__ == "__main__":
    e6 = E6("a", "k")

    node, logs = best_first(e6, heuristic)
    if node:
        print("TREE:")
        print_tree(node.get_root())
    print_solution(node, logs)
