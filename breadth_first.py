from node import Node
from container import Queue

def expand(problem, node):
    s = node.state
    for action in problem.actions(s):
        s_ = problem.result(action)
        cost = node.path_cost + problem.action_cost(action)
        yield Node(state=s_, parent=node, action=action, path_cost=cost)

def breadth_first(problem):  
    root = Node(state=problem.initial)

    logs = []

    if problem.is_goal(root.state):
        return root, logs

    q = Queue()
    q.insert(root)
    logs.append((f"{root} inserted in QUEUE", q.copy()))

    reached = [] 
    reached.append(root.state)
    logs.append((f"{root.state} inserted in REACHED", reached.copy()))

    while not q.is_empty():
        node = q.remove()
        logs.append((f"{node} removed from QUEUE", q.copy()))

        for child in expand(problem, node):
            s = child.state

            if problem.is_goal(s):
                return child, logs

            if child.state not in reached:
                q.insert(child)
                logs.append((f"{child} inserted in QUEUE", q.copy()))

                reached.append(child.state)
                logs.append((f"{child.state} inserted in REACHED", reached.copy()))

    return None, logs
