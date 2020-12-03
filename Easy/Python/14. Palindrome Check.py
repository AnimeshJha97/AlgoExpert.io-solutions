# O(n) -> Time | O(n) -> Space
# Recursive function call
def palinCheck(a, i=0):
    j = len(a) - 1 - i
# if a[i] == a[j] returns False, string is not palindrome else return True 
    return True if i >= j else a[i] == a[j] and palinCheck(a, i+1)

# O(n) -> Time | O(1) -> Space
def palinCheck(a):
    n = len(a)
    l = []
    i = 0
# Pushing the characters in the list
    while i < n//2:
        l.append(a[i])
        i += 1
    k = i - 1
# If length odd, increment i
    if n%2 != 0:
        i += 1
# Pop characters if match fould, else break as soon as not matched
    while i<n:
        if a[i] == a[k]
            l.pop()
            i += 1
            k -= 1
        else:
            break
# If list l is empty, then palindrome, else not
    if len(l) is 0:
        return True
    else:
        return False

ar = list(input())
print(palinCheck(ar))
