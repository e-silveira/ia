from minimax import Tree, minimax, minimax_pruned, minimax_pruned_r
import math


def make_tree(n: int, is_max: bool = True) -> Tree:
    """
    Cria a árvore do problema do palito.
    n: o número de palitos disponíveis
    """
    if n == 0:
        return Tree(-1 if is_max else 1, [])

    children: list[Tree] = []

    for m in range(1, 4):
        if n - m < 0:
            break
        children.append(make_tree(n - m, not is_max))

    return Tree(math.nan, children)


if __name__ == "__main__":
    # Minimax
    t = make_tree(5)
    minimax(t)
    t.print()

    # Minimax alpha-beta desde a esquerda.
    t = make_tree(5)
    minimax_pruned(t)
    t.print()

    # Minimax alpha-beta desde a direita.
    t = make_tree(5)
    minimax_pruned_r(t)
    t.print()
