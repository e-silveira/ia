from typing import Optional, Any


class Node:
    def __init__(
        self,
        state: Any,
        parent: Optional["Node"] = None,
        action: Optional[Any] = None,
        path_cost: int = 0,
    ):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __str__(self):
        return "{{{}, {}}}".format(self.state, self.path_cost)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, node):
        return self.state == node.state

    def to_root(self):
        path = []
        node = self
        while node.parent:
            path.append(node.action)
            node = node.parent
        path.reverse()
        return path
