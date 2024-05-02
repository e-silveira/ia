from e6 import E6, heuristic
from best_first import best_first
from help import print_solution
from node import print_tree

if __name__ == "__main__":
    e6 = E6("a", "k")

    node, logs = best_first(e6, lambda node: node.path_cost + heuristic(node))
    if node:
        print("TREE:")
        print_tree(node.get_root())
    print_solution(node, logs)
