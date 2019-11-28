from collections import defaultdict

nodes = defaultdict(lambda: None)
def cloneGraph(root):
    if root is None:
        return None
    if root.val in nodes:
        return nodes[root.val]
    new_node = Node(root.val)
    nodes[new_node.val] = node
    for a in root.adj:
        new_node.append(cloneGraph(a))
    return new_node
