from tree import Tree
from math import inf
from pprint import pprint

def make_tree(n):
    def __make_tree(n, parent, f):
        tree = Tree((None, n), parent)
        if n == 0:
            tree = Tree((1 if f == max else -1, n), parent)

        i = 1
        while n - i >= 0 and i <= 3:
            tree.child(__make_tree(n - i, tree, max if f == min else min))
            i += 1

        return tree

    return __make_tree(n, None, max)

def print_tree(root):
    shift = 4
    def __print_tree(tree, spaces):
        print(f"{' ' * spaces}{tree}")
        for child in tree.children:
            __print_tree(child, spaces + shift)
    __print_tree(root, 0)

def minimax(root):
    logs = []

    shift = 1
    spaces = [0]

    def __minimax(tree, f):
        if len(tree.children) == 0:
            logs.append(f"{'|   ' * (spaces[0] + shift)}{tree} returns {tree.value}")
            tree.value = (1 if f == max else -1, 0)
            return tree.value[0]

        values = []

        logs.append(f"{'|   ' * spaces[0]}{tree} opened")

        spaces[0] += shift
        
        for child in tree.children:
            value = __minimax(child, max if f == min else min)

            values.append(value)

        spaces[0] -= shift 

        tree.value = (f(values), tree.value[1])
        logs.append(f"{'|   ' * spaces[0]}{tree} gets value {tree.value} by {'max' if f == max else 'min'}")

        return tree.value[0]

    return __minimax(root, max), logs

def minimax_alpha_beta(root):

    logs = []

    shift = 1
    spaces = [0]

    def min_value(tree, alpha, beta):
        if len(tree.children) == 0:
            logs.append(f"{'|   ' * (spaces[0])}{tree} returns {tree.value[0]}")
            return tree.value[0]

        v = inf
        
        logs.append(f"{'|   ' * spaces[0]}{tree} opened")

        spaces[0] += shift

        for child in tree.children:
            v_ = max_value(child, alpha, beta)

            if v_ < v:
                v = v_
                beta = min(beta, v)
            if v <= alpha:
                spaces[0] -= shift
                tree.value = (v, tree.value[1])
                logs.append(f"{'|   ' * spaces[0]}{tree} closed prematurely with {v} <= {alpha} (alpha)")
                return v

        spaces[0] -= shift
        tree.value = (v, tree.value[1])
        logs.append(f"{'|   ' * spaces[0]}{tree} closed with value {v}")
        return v

    def max_value(tree, alpha, beta):
        if len(tree.children) == 0:
            logs.append(f"{'|   ' * (spaces[0] + shift)}{tree} returns {tree.value[0]}")
            return tree.value[0]

        v = -inf

        logs.append(f"{'|   ' * spaces[0]}{tree} opened")

        spaces[0] += shift
        
        for child in tree.children:
            v_ = min_value(child, alpha, beta)
            if v_ > v:
                v = v_
                alpha = max(alpha, v)
            if v >= beta:
                spaces[0] -= shift
                tree.value = (v, tree.value[1])
                logs.append(f"{'|   ' * spaces[0]}{tree} closed prematurely with {v} >= {beta} (beta)")
                return v

        spaces[0] -= shift
        tree.value = (v, tree.value[1])
        logs.append(f"{'|   ' * spaces[0]}{tree} closed with value {v}")
        return v

    return max_value(root, -inf, inf), logs

def rminimax_alpha_beta(root):

    logs = []

    shift = 1
    spaces = [0]

    def min_value(tree, alpha, beta):
        if len(tree.children) == 0:
            logs.append(f"{'|   ' * (spaces[0])}{tree} returns {tree.value[0]}")
            return tree.value[0]

        v = inf
        
        logs.append(f"{'|   ' * spaces[0]}{tree} opened")

        spaces[0] += shift

        for child in tree.children[::-1]:
            v_ = max_value(child, alpha, beta)

            if v_ < v:
                v = v_
                beta = min(beta, v)
            if v <= alpha:
                spaces[0] -= shift
                tree.value = (v, tree.value[1])
                logs.append(f"{'|   ' * spaces[0]}{tree} closed prematurely with {v} <= {alpha} (alpha)")
                return v

        spaces[0] -= shift
        tree.value = (v, tree.value[1])
        logs.append(f"{'|   ' * spaces[0]}{tree} closed with value {v}")
        return v

    def max_value(tree, alpha, beta):
        if len(tree.children) == 0:
            logs.append(f"{'|   ' * (spaces[0])}{tree} returns {tree.value[0]}")
            return tree.value[0]

        v = -inf

        logs.append(f"{'|   ' * spaces[0]}{tree} opened")

        spaces[0] += shift
        
        for child in tree.children[::-1]:
            v_ = min_value(child, alpha, beta)
            if v_ > v:
                v = v_
                alpha = max(alpha, v)
            if v >= beta:
                spaces[0] -= shift
                tree.value = (v, tree.value[1])
                logs.append(f"{'|   ' * spaces[0]}{tree} closed prematurely with {v} >= {beta} (beta)")
                return v

        spaces[0] -= shift
        tree.value = (v, tree.value[1])
        logs.append(f"{'|   ' * spaces[0]}{tree} closed with value {v}")
        return v
    return max_value(root, -inf, inf), logs

if __name__ == "__main__":
    tree = make_tree(5)
    print("MINIMAX")
    value, logs = minimax(tree)
    print(value)
    for log in logs:
        print(log)

    print("MINIMAX ALPHA-BETA LEFT")
    tree = make_tree(5)
    value, logs = minimax_alpha_beta(tree)
    print(value)
    for log in logs:
        print(log)

    print("MINIMAX ALPHA-BETA RIGHT")
    tree = make_tree(5)
    value, logs = rminimax_alpha_beta(tree)
    print(value)
    for log in logs:
        print(log)
