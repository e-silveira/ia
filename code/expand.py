def expand(problem, parent):
    state = parent.state
    ns = []
    for action in problem.actions(state):
        new_state = problem.result(action)
        cost = parent.path_cost + problem.action_cost(action)
        ns.append(parent.child(new_state, parent, action, cost))
    return ns

# Antigo do livro.
# def expand(problem, node):
#     s = node.state
#     for action in problem.actions(s):
#         s_ = problem.result(action)
#         cost = node.path_cost + problem.action_cost(action)
#         yield node.child(state=s_, parent=node, action=action, path_cost=cost)
