class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Tree():
	def __init__(self):
		self.rootNode = self.createBalancedTree()

def createBalancedTree(v):
    n = len(v)
    if n == 0:
        return None
    mid = (n - 1) // 2
    root = Node(v[mid])

    q = [(root, (0, n - 1))]

    while q:
        c, (s, e) = q.pop(0)
        i = s + (e - s) // 2

        if s < i:
            ml = s +(i - 1 - s) // 2
            l = Node(v[ml])
            c.left = l
            q.append((l, (s, i-1)))
        
        if e > i:
            mr = (i + 1 + (e - i - 1)) // 2
            r = Node(v[mr])
            c.right = r
            q.append((r, (i + 1, e)))

    return root

def binary_search(self, target, root=self.rootNode, depth=2):
    print(f"Checked {depth} Nodes")
	if [root.left, root.right] == [None, None]:
    	return None
	if target in [root.left.value, root.right.value]:
    	if target == root.left.value:
            return root.left, root
        else:
            return root.right, root
	if target < root.left.value:
        return binary_search(target, root.left.left, depth=depth+2)
    if target > root.right.value:
        return binary_search(target, root.right.right, depth=depth+2)

def remove_node(self, target):
    parent, node = binary_search(target)
    left = (parent.left == node)
    if node.left == None and node.right == None:
        if left:
            parent.left = None
        else:
            parent.right = None
        return

    if node.left != None and node.right == None:
        if left:
            parent.left = node.left
        else:
            parent.right = node.left
        return

    if node.right != None and node.left == None:
        if left:
            parent.left = node.right
        else:
            parent.right = node.right
        return

    #wanted by the question?
    if node.right != None and node.left != None:
        if left:
            node.left.right = node.right
            parent.left = node.left
        if right:
            node.right.left = node.left
            parent.right = node.right