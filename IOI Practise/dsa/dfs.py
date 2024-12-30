class Node():
    val = 0
    edges = []

    def __init__(self, v=0, e=[]):
        self.val = v
        self.edges = e

    def __str__(self):
        return str(self.val) + str(self.edges) 

seen = {}
pos = 0

def dfs(t: int, head: Node):
    global pos

    if head.val == t:
        return pos
    else:
        pos += 1
        res = list(filter(lambda x: x != -1, [dfs(t, i) for i in head.edges]))
        return min(res) if res != [] else -1

a = Node(3)
b = Node(6, [a])
c = Node(7, [a,b])
d = Node(2, [c])

print(dfs(2,d))