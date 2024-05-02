from problem import Problem
from depth_first import depth_first
from node import print_tree
from help import print_solution

class E3(Problem):
    def actions(self, state):
        (farmer, wolf, sheep, cabbage) = state

        actions = []

        if farmer == "l":
            if wolf != sheep and sheep != cabbage:
                actions.append(
                    ("go", ("l", wolf, sheep, cabbage), ("r", wolf, sheep, cabbage))
                )

            if sheep != cabbage:
                actions.append(
                    (
                        "carry-wolf",
                        ("l", "l", sheep, cabbage),
                        ("r", "r", sheep, cabbage),
                    )
                )

            actions.append(
                ("carry-sheep", ("l", wolf, "l", cabbage), ("r", wolf, "r", cabbage))
            )

            if wolf != sheep:
                actions.append(
                    ("carry-cabbage", ("l", wolf, sheep, "l"), ("r", wolf, sheep, "r"))
                )

        if farmer == "r":
            if wolf != sheep and sheep != cabbage:
                actions.append(
                    (
                        "go-back",
                        ("r", wolf, sheep, cabbage),
                        ("l", wolf, sheep, cabbage),
                    )
                )

            if sheep != cabbage:
                actions.append(
                    (
                        "bring-wolf",
                        ("r", "r", sheep, cabbage),
                        ("l", "l", sheep, cabbage),
                    )
                )

            actions.append(
                ("bring-sheep", ("r", wolf, "r", cabbage), ("l", wolf, "l", cabbage))
            )

            if wolf != sheep:
                actions.append(
                    ("bring-cabbage", ("r", wolf, sheep, "r"), ("l", wolf, sheep, "l"))
                )

        return actions

    def action_cost(self, action):
        return 1

    def result(self, action):
        (_, _, state) = action
        return state

    def is_goal(self, state):
        return state == ("r", "r", "r", "r")

if __name__ == "__main__":
    e3 = E3(("l", "l", "l", "l"), ("r", "r", "r", "r"))

    node, logs = depth_first(e3)

    if node:
        print("TREE:")
        print_tree(node.get_root())
        print_solution(node, logs)
