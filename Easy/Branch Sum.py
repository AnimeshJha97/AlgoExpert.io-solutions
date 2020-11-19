class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSum(root):
    li = []
    helper(root, li, sum = 0)
    print(li)
    return li

def helper(root, li, sum):
    sum += root.value
    
    if root.left:
        helper(root.left, li, sum)

    if root.right:
        helper(root.right, li, sum)

    if not root.right and not root.left :
        li.append(sum)
