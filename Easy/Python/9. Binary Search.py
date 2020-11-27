def binarySearch(ar, target):
    return helper(ar, target, 0, len(ar))

def helper(ar, target, start, end):
    mid = int((start + end) / 2)
    print("Start: " + str(start) + ",  End: " + str(end))
    if target is ar[mid]:
        return True
    elif target < ar[mid]:
        return helper(ar, target, start, mid-1)
    elif target > ar[mid]:
        return helper(ar, target, mid+1, end)
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




    
