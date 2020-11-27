# O(2^n) -> Time | O(n) -> Space
# Similar Recursive calls increases Time complexity
def fib(n):
    if n = 1:
        return 0
    elif n = 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

# O(n) -> Time | O(n) -> Space
# Memorization reduces similar recursive calls by directly fetching the value
def fib(n, mem = {1 : 0, 2 : 1}):
    if n in mem:
        return mem[n]
    else:
        mem[n] = fib(n-2, mem) + fib(n-1, mem)
        return mem[n]

# O(n) -> Time | O(1) -> Space
def fib(n):
    lastFib = [0, 1]
    c = 3
    while c <= n:
        nxt = lastFib[0] + lastFib[1]
        lastFib[0] = lastFib[1]
        lastFib[1] = nxt
        c += 1

    return lastFib[1] if n>1 else 0

print(fib(6))
