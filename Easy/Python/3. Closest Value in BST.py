#You are given a BST data structure consisting of BST nodes. Each BST node
#has an integer value stored in a property called "value" and two children
#nodes stored in properties called "left" and "right," respectively. A node
#is said to be a BST node if and only if it satisfies the BST property: its
#value is strictly greater than the values of every node to its left; its
#value is less than or equal to the values of every node to its right; and
#both of its children nodes are either BST nodes themselves or None (null)
#values. You are also given a target integer value; write a function that
#finds the closest value to that target value contained in the BST. Assume
#that there will only be one closest value.

class node :
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def closestValueInBST(tree, target):
    return closestValueInBSTHelper(tree, target, float("inf"))

# Recurssive Method
# Avg Time -> O(log n) | Space -> O(log n)
# Worst Tiem -> O(n)   | Space -> O(n)
# Space is not constant because we us the stack space
def closestValueInBSTHelper(tree, target, closest):
    if tree is None:
        return closest

    if(abs(tree.value - target) < abs(closest - target)):
        closest = tree.value

    if(target < tree.value):
        return closestValueInBSTHelper(tree.left, target, closest)
    elif(target > tree.value):
        return closestValueInBSTHelper(tree.right, target, closest)
    else:
        return closest


# Iterative Method
# Time -> O(log n) | Space -> O(1)
def closestValueInBST(tree, target):
    return closestValueInBSTHelper(tree, target, float("inf"))

def closestValueInBSTHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if(abs(currentNode.value - target) < abs(closest - target)):
            closest = currentNode.value
        if(target < currentNode.value):
            currentNode = currentNode.left
        elif(target > currentNode.value):
            currentNode = currentNode.right
        else:
            break;

    return closest
