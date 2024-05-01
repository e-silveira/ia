from problem import Problem
from best_first import best_first
from breadth_first import breadth_first
from depth_first import depth_first
from help import print_solution


class E5(Problem):
    def actions(self, state):
        actions = {
            "a": [("b", 1), ("c", 9), ("d", 4)],
            "b": [("a", 1), ("c", 7), ("e", 6), ("f", 1)],
            "c": [("a", 9), ("b", 7), ("f", 7)],
            "d": [("a", 4), ("f", 4), ("g", 5)],
            "e": [("b", 6), ("h", 9)],
            "f": [("b", 1), ("c", 7), ("d", 4), ("h", 4)],
            "g": [("d", 5), ("h", 1)],
            "h": [("e", 9), ("f", 4), ("g", 1)],
        }

        return actions.get(state, [])

    def action_cost(self, action):
        (_, cost) = action
        return cost

    def result(self, action):
        (state_, _) = action
        return state_

    def is_goal(self, state):
        return state == self.goal


def heuristic(node):
    return node.action[1] if node.parent else 0


if __name__ == "__main__":
    e5 = E5("a", "h")

    node, logs = best_first(e5, heuristic)
    print_solution(node, logs)

    node, logs = breadth_first(e5)
    print_solution(node, logs)

    node, logs = depth_first(e5)
    print_solution(node, logs)
