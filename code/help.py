from pprint import pprint
from node import print_tree

def print_solution(node, logs):
    if node:
        print("TREE:")
        print_tree(node.get_root())
        print(f"FOUND GOAL:\n{node} with cost {node.path_cost}")

        print("SOLUTION:")
        pprint(node.to_root())


    print("HISTORY:")
    for action, state in logs:
        print(action)
        pprint(state)
        print("---")

