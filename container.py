from abc import ABC, abstractmethod

class Container(ABC):
    def __init__(self):
        self.lst = [] 

    def __str__(self):
        return self.lst.__str__()

    def __repr__(self):
        return self.lst.__repr__()

    def empty(self):
        return len(self.lst) == 0

    def copy(self):
        return self.lst.copy()

    @abstractmethod
    def insert(self, value):
        pass
    
    @abstractmethod
    def remove(self):
        pass

class Queue(Container):
    def __init__(self):
        super().__init__()

    def is_empty(self):
        return len(self.lst) == 0

    def insert(self, value):
        self.lst.append(value)

    def remove(self):
        return self.lst.pop(0)

class Stack(Container):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        self.lst.append(value)

    def remove(self):
        return self.lst.pop()

class PriorityQueue:
    def __init__(self):
        self.lst = []

    def copy(self):
        return self.lst.copy()

    def empty(self):
        return len(self.lst) == 0

    def insert(self, p, value):
        for i, (p_, _) in enumerate(self.lst):
            if p < p_:
                self.lst.insert(i, (p, value))
                return 
        self.lst.append((p, value))

    def remove(self):
        (_, value) = self.lst.pop(0)
        return value

    def update(self, p, value):
        for i, (_, v) in enumerate(self.lst):
            if value == v:
                self.lst.pop(i)
                self.insert(p, value)
                return
