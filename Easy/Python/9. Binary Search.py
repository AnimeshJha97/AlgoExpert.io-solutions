def binarySearch(ar, target):
    return helper(ar, target, 0, len(ar)-1)

# Recursive method
# O(log n) -> Time | O(log n) -> Space
def helper(ar, target, start, end):
    mid = (start + end) // 2
    print("Start: " + str(start) + ",  End: " + str(end))
    if target is ar[mid]:
        return True
    elif target < ar[mid]:
        return helper(ar, target, start, mid-1)
    elif target > ar[mid]:
        return helper(ar, target, mid+1, end)
    else:
        return False

# Iterative method
# O(log n) -> Time | O(1) -> Space 
def helper(ar, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target is ar[mid]:
            return True
        elif target < ar[mid]:
            end = mid-1
        elif target > ar[mid]:
            start = mid+1
        else:
            return False

a = input()
a = list(map(int, a.split(' ')))
a.sort()
t = int(input())
if(binarySearch(a, t)):
    print("Element Present in the array")
else:
    print("Element Not Present in the array")
