# O(n^2) -> Time | O(1) -> Space
# So, what we do is, we consider a sorted array and an unsorted array without actually creating another array.
# Selection sort algo is inplace and so we need to mutate the given list of integers.
# Initially, the given array is not sorted, so their is no element in the sorted array.
# Let us consider a ptr initially at index 0.
# Lets iterate the while loot untill the ptr = len(ar)
# inside the while loop, first we find the minimum integer and then we swap the positions
# of the minimum with at of the integer at our ptr, initially 0.
# This will locate the min of all in the first place, and then we increment the ptr by 1,
# which will now bw at index 1. The second min will now be at index 1, and so on untill we get our sorted array.
def selectionSort(a):
    n = len(a)
    ptr = 0
    while ptr < n:
        imin = indexMin(a, ptr, n)
        a[ptr], a[imin] = a[imin], a[ptr]
        ptr += 1
    return a

def indexMin(a, s, e):
    min = float('inf')
    k = 0
    for i in range(s, e):
        if a[i] < min:
            min = a[i]
            k = i
    return k

ar = input()
ar = list(map(int, ar.split(' ')))
print(selectionSort(ar))
