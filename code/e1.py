from itertools import product
from problem import Problem
from breadth_first import breadth_first_with_logs
from help import print_solution

def apply_transition(state, transition):
    (m, c) = transition

    if state[2] == 0:
        return (state[0] - m, state[1] - c, 1)

    return (state[0] + m, state[1] + c, 0)


def valid_transition(state, transition, m_t, c_t):
    (m, c, _) = apply_transition(state, transition)

    m_, c_ = m_t - m, c_t - c

    return (m >= c or m == 0) and (m_ >= c_ or m_ == 0)

def add_side(transition, side):
    (m, c) = transition
    return (m, c, 0 if side == 1 else 1)

class E1(Problem):
    def __init__(self, initial, goal, m_t, c_t, boat_size):
        super().__init__(initial, goal)
        self.m_t = m_t
        self.c_t = c_t
        self.boat_size = boat_size

    def actions(self, state):
        (m, c, side) = state

        if side == 0:
            transitions = product(range(m + 1), range(c + 1))
        else:
            transitions = product(range(self.m_t - m + 1), range(self.c_t - c + 1))

        transitions = filter(
            lambda t: t != (0, 0) and t[0] + t[1] <= self.boat_size, transitions
        )

        transitions = filter(lambda t: valid_transition(state, t, self.m_t, self.c_t), transitions)

        transitions = map(
            lambda t: (state, apply_transition(state, t), add_side(t, side), 1), transitions
        )

        return list(transitions)

    def action_cost(self, action):
        (_, _, _, cost) = action
        return cost

    def result(self, action):
        (_, state, _, _) = action
        return state

    def is_goal(self, state):
        return state == self.goal

if __name__ == "__main__":
    e1 = E1((3, 3, 0), (0, 0, 1), 3, 3, 2)

    node, logs = breadth_first_with_logs(e1)
    print_solution(node, logs)
