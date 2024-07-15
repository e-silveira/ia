from e6 import E6, heuristic
from best_first import best_first_with_logs
from help import print_solution

if __name__ == "__main__":
    e6 = E6("a", "k")

    node, logs = best_first_with_logs(e6, lambda node: node.path_cost + heuristic(node))
    print_solution(node, logs)
