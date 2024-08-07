class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data > root.data:
                cur = self.insert(root.right, data)
                root.right = cur
            else:
                cur = self.insert(root.left, data)
                root.left = cur
        return root

    def getHeight(self, root):
        # Write your code here
        if root is None:
            return 0
        else:
            return 1 + max(self.getHeight(root.right), self.getHeight(root.left))

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)

height = myTree.getHeight(root)
print(height)


def tree_deep(length: int, sp: list) -> int:
    height = 1
