from problem import Problem
from best_first import best_first_with_logs
from help import print_solution


def get_indices(goal_matrix, nrow, ncol, value):
    """
    Retorna os índices de `value` na `goal_matrix`.

    Essa função é usada para calcular a distância entre o local
    do valor na matriz de objetivo e na matriz do estado atual.

    goal_matrix: matriz de objetivo
    nrow: número de linhas
    ncol: número de colunas
    value: valor que estamos procurando (da matriz de estado).
    """
    for i in range(nrow):
        for j in range(ncol):
            if goal_matrix[i * ncol + j] == value:
                return i, j


def move(state, ncol, i, j, i_, j_):
    """
    Faz o swap entre posições na matriz de estado.
    """
    state = list(state)
    state[i * ncol + j] = state[i_ * ncol + j_]
    state[i_ * ncol + j_] = 0
    return tuple(state)


def moves(state, nrow, ncol):
    """
    Retorna os possíveis movimentos de acordo com a posição de 0.
    """
    def moves(i, j):
        moves = []

        if i > 0:
            moves.append(move(state, ncol, i, j, i - 1, j))
        if i < nrow - 1:
            moves.append(move(state, ncol, i, j, i + 1, j))
        if j > 0:
            moves.append(move(state, ncol, i, j, i, j - 1))
        if j < ncol - 1:
            moves.append(move(state, ncol, i, j, i, j + 1))

        return moves

    indices = get_indices(state, nrow, ncol, 0)
    if indices:
        i, j = indices
        return moves(i, j)

    return []


class E8(Problem):
    def __init__(self, state, goal, nrow, ncol):
        super().__init__(state, goal)
        self.nrow = nrow
        self.ncol = ncol

    def actions(self, state):
        actions = moves(state, self.nrow, self.ncol)
        return actions

    def action_cost(self, action):
        return 1

    def result(self, action):
        return action

    def is_goal(self, state):
        return state == goal


def manhattan(i, j, i_, j_):
    return abs(i - i_) + abs(j - j_)


def make_heuristic(nrow, ncol, goal):
    """
    Cria a função heurística de acordo com o tamanho
    da matriz e o estado objetivo.
    """
    def heuristic(node):
        state = node.state
        mdist = 0
        for i in range(nrow):
            for j in range(ncol):
                if state[i * ncol + j] == 0:
                    continue
                indices = get_indices(goal, nrow, ncol, state[i * ncol + j])
                if indices:
                    i_, j_ = indices
                    mdist += manhattan(i, j, i_, j_)

        return mdist

    return heuristic


if __name__ == "__main__":
    goal = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    heuristic = make_heuristic(3, 3, goal)

    state = (1, 3, 4, 8, 2, 5, 7, 6, 0)
    e8 = E8(state, goal, 3, 3)

    print("+++ GREEDY BEST FIRST - COST 1 +++")
    node, logs = best_first_with_logs(e8, lambda _: 1)
    print_solution(node, logs)

    print("+++ GREEDY BEST FIRST - HEURISTIC +++")
    node, logs = best_first_with_logs(e8, heuristic)
    print_solution(node, logs)

    print("+++ A* +++")
    state = (1, 2, 3, 0, 6, 4, 8, 7, 5)
    e8b = E8(state, goal, 3, 3)
    node, logs = best_first_with_logs(e8, lambda node: node.path_cost + heuristic(node))
    print_solution(node, logs)
