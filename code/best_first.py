from node import Node
from expand import expand
from container import PriorityQueue


def best_first(problem, h):
    node = Node(state=problem.initial, path_cost=0)

    logs = []

    pq = PriorityQueue()
    reached = {}

    pq.insert(0, node)
    logs.append((f"{node} inserted in PRIORITY QUEUE with priority {0}", pq.copy()))

    reached[node.state] = node
    logs.append(
        (
            f"{node.state} inserted in REACHED with value {node.path_cost}",
            reached.copy(),
        )
    )

    while not pq.empty():
        node = pq.remove()
        logs.append((f"{node} removed from PRIORITY QUEUE", pq.copy()))

        if problem.is_goal(node.state):
            return node, logs

        for child in expand(problem, node):
            s = child.state

            if s not in reached:
                reached[s] = child
                logs.append(
                    (
                        f"{s} inserted in REACHED with value {child.path_cost}",
                        reached.copy(),
                    )
                )

                pq.insert(h(child), child)
                logs.append(
                    (
                        f"{child} inserted in PRIORITY QUEUE with priority {h(child)}",
                        pq.copy(),
                    )
                )

            elif child.path_cost < reached[s].path_cost:
                reached[s] = child
                logs.append(
                    (
                        f"{s} updated in REACHED with value {child.path_cost}",
                        reached.copy(),
                    )
                )

                pq.update(h(child), child)
                logs.append(
                    (
                        f"{child} update in PRIORITY QUEUE with priority {h(child)}",
                        pq.copy(),
                    )
                )

    return None, logs
