"""
 Given two arrays, calculate the minimum difference between the elements
 of arrays and return that pair of elements

 Example :
 I/p:
 [-1 5 10 20 28 3]
 [26 134 135 15 35]
 O/p:
 [28, 26]
"""

"""
Approch 1 : The naive method to traverse every element of both array
compare the difference and storing the elements in min array
"""
# O(n*m) -> Time | O(1) -> Space


"""
 Approch 2(Optimal):

 So what we do here is, we first sort the array.
 Then we have two pointers i and j starting from 0 index
 [-1, 3, 5, 10, 20, 28]
  ^
  i
 [15, 20, 26, 134, 135]
  ^
  j

  1) We compare if the elements are equal, and if true, we return them
  else
  2) if array1[i] < array2[j], we calculate the difference
        if the difference is min, we write the value of elements in our returning list
        and update the value of difference
        Now, we increment i to i+1. This is done untill we get an element > array2[j]
  else
  3) is similar to 2) and j is incremented to j+1 untill we get an element > array1[i]

  Finally we return the list storing the pair.
"""

# O(nlogn + mlogm) -> Time | O(1) - > Space
# nlogn time to sort the list
def minDiff(s1, s2)
    s1.sort()
    s2.sort()

    a = [0,0]
    i, j = 0, 0
    diff = float(inf)

    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            a[0], a[1] = s1[i], s1[i]
            diff = 0
            break
        elif s1[i] < s2[j]:
            if diff > s2[j] - s1[i]:
                diff = s2[j] - s1[i]
                a[0], a[1] = s1[i], s2[j]
            i += 1
        else:
            if diff > s1[i] - s2[j]:
                diff = s1[i] - s2[j]
                a[0], a[1] = s1[i], s2[j]
            j += 1
    return a

s1 = input()
s1 = list(map(int, s1.split(' ')))
s2 = input()
s2 = list(map(int, s2.split(' ')))
print(minDiff(s1, s2))
