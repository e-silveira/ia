from tree import Tree
from math import inf
from pprint import pprint

# A função de utilidade pode simplesmente dar pop na lista de valores dos nodos-folha.


def make_binary_tree(height):
    def _make_binary_tree(parent, height):
        if height == 0:
            leaf = Tree(None, parent)
            return leaf

        t = Tree(None, parent)

        t.child(_make_binary_tree(t, height - 1))
        t.child(_make_binary_tree(t, height - 1))

        return t

    root = Tree(None, None)
    return _make_binary_tree(root, height)


def add_leaf_values(tree, values):
    if len(tree.children) == 0:
        tree.value = values.pop(0)

    for child in tree.children:
        add_leaf_values(child, values)


def minimax(root):
    logs = []

    shift = 4
    spaces = [0]

    logs.append(f"{root} opened")

    def __minimax(tree, f):
        if len(tree.children) == 0:
            logs.append(f"{' ' * (spaces[0] + shift)}{tree} returns {tree.value}")
            return tree.value, [] 

        values = []
        paths = []

        spaces[0] += shift

        logs.append(f"{' ' * spaces[0]}{tree} opened")
        
        for child in tree.children:
            value, path = __minimax(child, max if f == min else min)

            values.append(value)
            paths.append(path)

        spaces[0] -= shift 

        tree.value = f(values)
        logs.append(f"{' ' * spaces[0]}{tree} gets value {tree.value} by {'max' if f == max else 'min'}")

        path = paths[values.index(tree.value)]
        path.append(tree)

        return tree.value, path 

    return __minimax(root, max), logs

def minimax_alpha_beta(root):

    logs = []

    shift = 4
    spaces = [0]

    logs.append(f"{root} opened")

    def min_value(tree, alpha, beta):
        if len(tree.children) == 0:
            logs.append(f"{' ' * (spaces[0] + shift)}{tree} returns {tree.value}")
            return tree.value

        v = inf
        
        spaces[0] += shift

        logs.append(f"{' ' * spaces[0]}{tree} opened")

        for child in tree.children:
            v_ = max_value(child, alpha, beta)

            if v_ < v:
                v = v_
                beta = min(beta, v)
            if v <= alpha:
                spaces[0] -= shift
                logs.append(f"{' ' * spaces[0]}{tree} closed prematurely with {v} <= {alpha} (alpha)")
                return v

        spaces[0] -= shift
        logs.append(f"{' ' * spaces[0]}{tree} closed with value {v}")
        return v

    def max_value(tree, alpha, beta):
        if len(tree.children) == 0:
            logs.append(f"{' ' * (spaces[0] + shift)}{tree} returns {tree.value}")
            return tree.value

        v = -inf

        spaces[0] += shift

        logs.append(f"{' ' * spaces[0]}{tree} opened")
        
        for child in tree.children:
            v_ = min_value(child, alpha, beta)
            if v_ > v:
                v = v_
                alpha = max(alpha, v)
            if v >= beta:
                spaces[0] -= shift
                logs.append(f"{' ' * spaces[0]}{tree} closed prematurely with {v} >= {beta} (beta)")
                return v

        spaces[0] -= shift
        logs.append(f"{' ' * spaces[0]}{tree} closed with value {v}")
        return v
    return max_value(root, -inf, inf), logs

def rminimax_alpha_beta(root):

    logs = []

    shift = 4
    spaces = [0]

    logs.append(f"{root} opened")

    def min_value(tree, alpha, beta):
        if len(tree.children) == 0:
            logs.append(f"{' ' * (spaces[0] + shift)}{tree} returns {tree.value}")
            return tree.value

        v = inf
        
        spaces[0] += shift

        logs.append(f"{' ' * spaces[0]}{tree} opened")

        for child in tree.children[::-1]:
            v_ = max_value(child, alpha, beta)

            if v_ < v:
                v = v_
                beta = min(beta, v)
            if v <= alpha:
                spaces[0] -= shift
                logs.append(f"{' ' * spaces[0]}{tree} closed prematurely with {v} <= {alpha} (alpha)")
                return v

        spaces[0] -= shift
        logs.append(f"{' ' * spaces[0]}{tree} closed with value {v}")
        return v

    def max_value(tree, alpha, beta):
        if len(tree.children) == 0:
            logs.append(f"{' ' * (spaces[0] + shift)}{tree} returns {tree.value}")
            return tree.value

        v = -inf

        spaces[0] += shift

        logs.append(f"{' ' * spaces[0]}{tree} opened")
        
        for child in tree.children[::-1]:
            v_ = min_value(child, alpha, beta)
            if v_ > v:
                v = v_
                alpha = max(alpha, v)
            if v >= beta:
                spaces[0] -= shift
                logs.append(f"{' ' * spaces[0]}{tree} closed prematurely with {v} >= {beta} (beta)")
                return v

        spaces[0] -= shift
        logs.append(f"{' ' * spaces[0]}{tree} closed with value {v}")
        return v
    return max_value(root, -inf, inf), logs


if __name__ == "__main__":
    leafs = [20, 33, -45, 31, 24, 25, -10, 20, 40, -25, 18, -42, 24, -19, 36, -41]

    t = make_binary_tree(height=4)
    add_leaf_values(t, leafs)

    (value, _), logs = minimax(t)
    value, logs = minimax_alpha_beta(t)
    pprint(value)
    pprint(logs)

    leafs = [20, 33, -45, 31, 24, 25, -10, 20, 40, -25, 18, -42, 24, -19, 36, -41]
    t = make_binary_tree(height=4)
    add_leaf_values(t, leafs)

    value, logs = rminimax_alpha_beta(t)
    pprint(value)
    pprint(logs)

