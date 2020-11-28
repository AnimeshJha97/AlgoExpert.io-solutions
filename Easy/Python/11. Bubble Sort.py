def swap(a,b):
    if a > b :
        return b, a
    else:
        return a, b

def bubbleSort(a):
    n = len(a)
    flag = 1

    while flag:
        flag = 0
        for i in range(0, n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = swap(a[i], a[i+1])
                flag = 1
        n -= 1
    return a

ar = input()
ar = list(map(int, ar.split(" ")))
print(bubbleSort(ar))
