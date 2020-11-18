# Using HashTable/Dictionary
# O(n) -> Time | O(n) -> Space
# Steps :
# 1) Create a dictionary/hashTable.
# 2) Iterate through the elements in the list.
# 3) If the value of the (given sum - element) is present in the dictionary
#    then return the pair, else initialize the value of the element(key) as true
#    which identifies that the element is present in the array.
# 4) In the end an empty list is returned which covers for if no pair is found.

def twoNumberSum(li, s):
    ht = {}
    l = len(li)
    i = 0
    for k in li:
        if (s - k) in ht :
            return [s-k, k]
        else :
            ht[k] = True
    return []

# Using Two pointers
# O(n) -> Time | O(1) -> Space
# Steps :
# 1) Sort the list.
# 2) Create two pointers pointing to the first and the last index of the list.
# 3) Loop from both the ends untill first pointer is less than the second pointer
#    or the sum is found.
# 4) If the sum is less than the required sum, the first pointer will be incremented
#    as smaller elements are present on the left side.
# 5) If the sum is greater than the required sum, than the second pointer will decrement.
# 6) If the sum is found, return the pair of elements else return empty list.

def twoNumberSum(li, s):
#1)
#   li = [int(i) for i in li]  for converting the string list to integer list before sorting.
    l = len(li)
    li.sort()
#2)
    i = 0
    j = l-1
#3),4),5),6)
    while(i < j):
        sum = int(li[i]) + int(li[j])
        if (sum == s):
            return [li[i], li[j]]
            break
        elif(sum < s):
            i += 1
        else :
            j -= 1
