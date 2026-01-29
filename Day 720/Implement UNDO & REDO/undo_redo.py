class Solution:
    def __init__(self):
        self.doc = ""
        self.redost = []

    def append(self, X):
        self.doc += X
        self.redost.clear()

    def undo(self):
        if self.doc:
            last = self.doc[-1]
            self.doc = self.doc[:-1]
            self.redost.append(last)

    def redo(self):
        if self.redost:
            ch = self.redost.pop()
            self.doc += ch

    def read(self):
        return self.doc