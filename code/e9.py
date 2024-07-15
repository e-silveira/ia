from minimax import Tree, minimax, minimax_pruned, minimax_pruned_r
from typing import Iterator
import math


def make_tree_from_iter(n: int, depth: int, it: Iterator[float]) -> Tree:
    """
    Cria uma árvore a partir de um iterador (depth-first).

    n: o número de filhos por nodo
    depth: a profundidade da árvore
    it: o iterador

    Esta função assume que o iterador vai preencher toda a última camada.
    Se ele terminar antes, ocorrerá um erro.
    """
    if depth == 0:
        return Tree(next(it), [])

    children: list[Tree] = []
    for _ in range(n):
        children.append(make_tree_from_iter(n, depth - 1, it))

    return Tree(math.nan, children)


if __name__ == "__main__":
    x = [20, 33, -45, 31, 24, 25, -10, 20, 40, -25, 18, -42, 24, -19, 36, -41]

    # Minimax
    y = iter(x.copy())
    t = make_tree_from_iter(2, 4, y)
    minimax(t)
    t.print()

    # Minimax alpha-beta desde a esquerda.
    y = iter(x.copy())
    t = make_tree_from_iter(2, 4, y)
    minimax_pruned(t)
    t.print()

    # Minimax alpha-beta desde a direita.
    y = iter(x.copy())
    t = make_tree_from_iter(2, 4, y)
    minimax_pruned_r(t)
    t.print()
