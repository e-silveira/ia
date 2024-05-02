class Tree:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.children = []

    def child(self, tree):
        self.children.append(tree)

    def __str__(self):
        return f"{{{self.value}}}"

    def __repr__(self):
        return self.__str__()
