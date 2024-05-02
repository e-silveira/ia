from problem import Problem
from breadth_first import breadth_first
from depth_first import depth_first
from node import print_tree
from help import print_solution

class E4(Problem):
    def actions(self, state):
        actions = {
            "a": [("a", "b", "taking 1", 1), ("a", "b", "taking 2", 1), ("a", "d", "taking 3", 1)],
            "b": [("b", "e", "taking 4", 1), ("b", "f", "taking 5", 1)],
            "c": [("c", "g", "taking 6", 1), ("c", "h", "taking 7", 1), ("c", "i", "taking 8", 1)],
            "d": [("d", "j", "taking 9", 1)],
            "e": [("e", "k", "taking 10", 1), ("e", "l", "taking 11", 1)],
            "g": [("g", "m", "taking 12", 1)],
            "j": [("j", "n", "taking 13", 1), ("j", "o", "taking 14", 1)],
            "k": [("k", "f", "taking 15", 1)],
            "l": [("l", "h", "taking 16", 1)],
            "m": [("m", "d", "taking 17", 1)],
            "o": [("o", "a", "taking 18", 1)],
            "n": [("n", "b", "taking 19", 1)],
        }

        return actions.get(state, [])

    def action_cost(self, action):
        (_, _, _, cost) = action
        return cost

    def result(self, action):
        (_, state, _, _) = action
        return state

    def is_goal(self, state):
        return state == self.goal

if __name__ == "__main__":

    e4 = E4("a", "j") 

    node, logs = breadth_first(e4)
    if node:
        print("TREE:")
        print_tree(node.get_root())
        print_solution(node, logs)

    print("--------------------------------------------------\n")

    node, logs = depth_first(e4)
    if node:
        print("TREE:")
        print_tree(node.get_root())
        print_solution(node, logs)
