from node import Node
from problem import Problem
from container import Queue
from expand import expand
from typing import Any


def breadth_first(problem: Problem) -> Node | None:
    root: Node = Node(state=problem.initial)

    if problem.is_goal(root.state):
        return root

    q: Queue = Queue()
    q.insert(root)

    reached: Any = []
    reached.append(root.state)

    while not q.is_empty():
        node: Node = q.remove()

        for child in expand(problem, node):
            s: Any = child.state

            if problem.is_goal(s):
                return child

            if child.state not in reached:
                q.insert(child)
                reached.append(child.state)

    return None


def breadth_first_with_logs(problem: Problem) -> tuple[Node | None, list]:
    root: Node = Node(state=problem.initial)

    logs = []

    if problem.is_goal(root.state):
        return root, logs

    q: Queue = Queue()
    q.insert(root)
    logs.append((f"{root} inserted in QUEUE", q.copy()))

    reached: list[Any] = []
    reached.append(root.state)
    logs.append((f"{root.state} inserted in REACHED", reached.copy()))

    while not q.is_empty():
        node: Node = q.remove()
        logs.append((f"{node} removed from QUEUE", q.copy()))

        for child in expand(problem, node):
            s: Any = child.state

            if problem.is_goal(s):
                return child, logs

            if child.state not in reached:
                q.insert(child)
                logs.append((f"{child} inserted in QUEUE", q.copy()))

                reached.append(child.state)
                logs.append((f"{child.state} inserted in REACHED", reached.copy()))

    return None, logs
