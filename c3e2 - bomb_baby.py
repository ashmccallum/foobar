# Generate Tree:
# 1) create node class with value, parent, left and right properties
class Node:
    def __init__(self, val):
        self.v = val
        self.r = None
        self.l = None

# 2) create tree class
class Tree:
    def __init__(self):
        self.root = None


    # create add method for starting root
    def add(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    # use _add for recursively filling tree
    # Q: Should I always create a left and right node to be a proper tree? It will mean having negative numbers
    def _add(self, val, node):
        if (val.m < 1 or val.f < 1):

        elif (val.m < val.f):

def answer(M, F):
    t = Tree()
    t.add({"m":M, "f":F})
    return

print answer(2,1)
print answer(4,7)