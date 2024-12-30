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
    if head in seen:
        return -1

    if head.val == t:
        return pos
    else:
        seen.update({str(head):True})
        pos += 1
        res = list(filter(lambda x: x != -1, [dfs(t, i) for i in head.edges]))
        return min(res) if res != [] else -1