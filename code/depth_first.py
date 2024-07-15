from node import Node
from expand import expand

def depth_first(problem):

    root = Node(problem.initial)

    logs = []
    reached = []

    reached.append(root.state)
    logs.append((f"{root.state} inserted in REACHED", reached.copy()))

    def _depth_first(node):

        if problem.is_goal(node.state):
            return node

        for child in expand(problem, node):
            if child.state not in reached:
                reached.append(child.state)
                logs.append((f"{child.state} inserted in REACHED", reached.copy()))

                result = _depth_first(child)

                if result:
                    return result

        return None

    return _depth_first(root), logs
