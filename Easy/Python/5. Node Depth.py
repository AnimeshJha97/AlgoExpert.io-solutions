class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def levelOrderInsertion(a, root, i, n):
    if i < n:
        temp = node(a[i])
        root = temp
        root.left = levelOrderInsertion(a, root.left, 2*i+1, n)
        root.right = levelOrderInsertion(a, root.right, 2*i+2, n)
    return root

def printTree(root):
    if root:
        printTree(root.left)
        print(root.value, end = ' ')
        printTree(root.right)

def depthSum(root, depth):
    if root:
        return depth + depthSum(root.left, depth+1) + depthSum(root.right, depth+1)
    else:
        return 0

if __name__ == '__main__':
    ar = [1,2,3,4,5,6,7,8,9]
    n = len(ar)
    root = None
    root = levelOrderInsertion(ar, root, 0, n)
    printTree(root)
    print()
    print(depthSum(root, 0))
