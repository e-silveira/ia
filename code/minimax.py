import math


class Tree:
    def __init__(self, value: float, children: list["Tree"]):
        self.value: float = value
        self.children: list["Tree"] = children
        self.pruned: bool = False

    def print(self, depth: int = 0):
        print(depth * "---|" + ("x" if self.pruned else str(self.value)))
        for child in self.children:
            child.print(depth + 1)

    def prune(self):
        self.pruned = True
        for child in self.children:
            child.prune()


def minimax(tree: Tree, maximize: bool = True) -> float:
    if len(tree.children) == 0:
        return tree.value

    if maximize:
        max_value = -math.inf
        for child in tree.children:
            max_value = max(max_value, minimax(child, False))
        tree.value = max_value
        return max_value
    else:
        min_value = math.inf
        for child in tree.children:
            min_value = min(min_value, minimax(child, True))
        tree.value = min_value
        return min_value


def minimax_pruned(
    tree: Tree,
    maximize: bool = True,
    alpha: float = -math.inf,
    beta: float = math.inf,
) -> float:
    if len(tree.children) == 0:
        return tree.value

    if maximize:
        max_value = -math.inf

        i = 0
        while i < len(tree.children):
            cur_value = minimax_pruned(tree.children[i], False, alpha, beta)
            max_value = max(max_value, cur_value)
            alpha = max(alpha, cur_value)
            if beta <= alpha:
                break
            i += 1

        while i < len(tree.children):
            tree.children[i].prune()
            i += 1

        tree.value = max_value
        return max_value
    else:
        min_value = math.inf

        i = 0
        while i < len(tree.children):
            cur_value = minimax_pruned(tree.children[i], True, alpha, beta)
            min_value = min(min_value, cur_value)
            beta = min(beta, cur_value)
            if beta <= alpha:
                break
            i += 1

        while i < len(tree.children):
            tree.children[i].prune()
            i += 1

        tree.value = min_value
        return min_value

def minimax_pruned_r(
    tree: Tree,
    maximize: bool = True,
    alpha: float = -math.inf,
    beta: float = math.inf,
) -> float:
    if len(tree.children) == 0:
        return tree.value

    if maximize:
        max_value = -math.inf

        i = len(tree.children) - 1
        while i >= 0:
            cur_value = minimax_pruned(tree.children[i], False, alpha, beta)
            max_value = max(max_value, cur_value)
            alpha = max(alpha, cur_value)
            if beta <= alpha:
                break
            i -= 1

        while i >= 0:
            tree.children[i].prune()
            i -= 1

        tree.value = max_value
        return max_value
    else:
        min_value = math.inf

        i = len(tree.children) - 1
        while i >= 0:
            cur_value = minimax_pruned(tree.children[i], True, alpha, beta)
            min_value = min(min_value, cur_value)
            beta = min(beta, cur_value)
            if beta <= alpha:
                break
            i -= 1

        while i >= 0:
            tree.children[i].prune()
            i -= 1

        tree.value = min_value
        return min_value
