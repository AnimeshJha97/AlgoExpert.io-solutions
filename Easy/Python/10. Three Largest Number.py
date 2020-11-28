# Sorted the array
# O(n*logn) -> Time | O(1) -> Time
def max3(a):
    a.sort()
    n = len(a)
    print(str(a[n-3]) + " " + str(a[n-2]) + " " + str(a[n-1]))

# Using a array of len 3 to store the result
# O(n) -> Time | O(1) - > Space
def max3(a):
    res = [None, None, None]
    for k in a:
        if res[2] is None or k > res[2]:
            res[0] = res[1]
            res[1] = res[2]
            res[2] = k
        elif res[1] is None or k > res[1]:
            res[0] = res[1]
            res[1] = k
        elif res[0] is None or k > res[0]:
            res[0] = k
    print(str(res[0]) + " " + str(res[1]) + " " + str(res[2]))

ar = input()
ar = list(map(int, ar.split(' ')))
max3(ar)
