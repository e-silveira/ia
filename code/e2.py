from breadth_first import breadth_first
from problem import Problem
from help import print_solution
from pprint import pprint
from node import print_tree

class E2(Problem):
    def actions(self, state):
        (x, y) = state

        actions = []

        if x < 3:
            actions.append(((3, y), "filling 3"))

        if y < 4:
            actions.append(((x, 4), "filling 4"))

        if x > 0:
            actions.append(((0, y), "emptying 3"))

        if y > 0:
            actions.append(((x, 0), "emptying 4"))

        if x > 0 and y < 4 and x + y <= 4:
            actions.append(((0, x + y), "pouring all 3 into 4"))

        if x > 0 and y < 4 and x + y > 4:
            actions.append(((x + y - 4, 4), "pouring some 3 into 4"))

        if x < 3 and y > 0 and x + y <= 3:
            actions.append(((x + y, 0), "pouring all 4 into 3"))

        if x < 3 and y > 0 and x + y > 3:
            actions.append(((3, x + y - 3), "pouring some 4 into 3"))

        actions = map(lambda t: (state, t[0], t[1], 1), actions)

        return list(actions)
    
    def action_cost(self,action):
        (_, _, _, cost) = action
        return cost 

    def result(self, action):
        (_, state, _, _) = action
        return state

    def is_goal(self, state):
        return state[1] == 2

if __name__ == "__main__":
    e2 = E2((0, 0), (None, 2))
    node, logs = breadth_first(e2)

    if node:
        print("TREE:")
        print_tree(node.get_root())
        print_solution(node, logs) 
