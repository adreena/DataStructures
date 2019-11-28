
class BSTIterator:
    def __init__(self, root):
        self.items = []
        self.origin = root
        self.getlefts(root)

    def getLefts(self,root)
        while root:
            self.items.append(root.val)
            root = root.left

    def hasNext(self):
        if len(items)>0:
            return True
        return False

    def next(self):
        if self.hasNext():
            top = self.items.pop()
            if top.right is not None:
                self.getLefts(top.right)
            return top.val
        return None
