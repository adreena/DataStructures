

head = Node(-1)
head.next = last
last = Node(-1)
last.prev = head

def ConvertBTLL(root):
    if root is None:
        return
    ConvertBTLL(root.left)
    new_node = Node(root.val)
    prev = last.prev
    prev.next = new_node
    new_node.next = last
    last.prev = new_node
    ConvertBTLL(root.right)

def main(root):
    if root is None:
        return None
    ConvertBTLL(root)
    head = head.next
    last = last.prev
    head.prev = last
    last.next = head
    return head
