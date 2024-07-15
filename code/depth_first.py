from node import Node
from problem import Problem
from expand import expand
from typing import Any


def depth_first(problem: Problem) -> Node | None:
    root: Node = Node(problem.initial)

    reached: Any = []
    reached.append(root.state)

    def __depth_first(node: Node) -> Node | None:
        if problem.is_goal(node.state):
            return node

        for child in expand(problem, node):
            if child.state not in reached:
                reached.append(child.state)
                result: Node | None = __depth_first(child)
                if result:
                    return result

        return None

    return __depth_first(root)

def depth_first_with_logs(problem: Problem) -> tuple[Node | None, list]:
    root: Node = Node(problem.initial)

    logs = []
    reached: list[Any] = []

    reached.append(root.state)
    logs.append((f"{root.state} inserted in REACHED", reached.copy()))

    def __depth_first(node):
        if problem.is_goal(node.state):
            return node

        for child in expand(problem, node):
            if child.state not in reached:
                reached.append(child.state)
                logs.append((f"{child.state} inserted in REACHED", reached.copy()))

                result: Node | None = __depth_first(child)
                if result:
                    return result

        return None

    return __depth_first(root), logs
