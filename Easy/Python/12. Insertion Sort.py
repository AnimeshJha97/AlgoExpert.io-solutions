# O(n^2) -> Time | O(1) -> Space
def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        k = i
        while k > 0 and a[k] <= a[k-1]:
            a[k], a[k-1] = a[k-1], a[k]
            k -= 1
    return a

ar = input()
ar = list(map(int, ar.split(' ')))
print(insertionSort(ar))
