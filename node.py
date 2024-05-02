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
        self.children = []

    def __str__(self):
        return "{{{}, {}}}".format(self.state, self.path_cost)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, node):
        return self.state == node.state

    def child(self, state, parent, action, path_cost):
        node = Node(state, parent, action, path_cost)
        self.children.append(node)
        return node

    def get_root(self):
        node = self
        while node.parent:
            node = node.parent
        return node 

    def to_root(self):
        path = []
        node = self
        while node.parent:
            path.append(node.action)
            node = node.parent
        path.reverse()
        return path

def print_tree(root):
    def __print_tree(node, height):
        print(f"{'|   ' * height}{node}")
        for child in node.children:
            __print_tree(child, height + 1)
    __print_tree(root, 0)
