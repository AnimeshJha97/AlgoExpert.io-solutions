arr = input().split()
seq = input().split()

i = j = c = 0

while(i < len(arr) and j < len(seq)):
    if (arr[i] == seq[j]) :
        c += 1
        i += 1
        j += 1
    else:
        i += 1

if c == len(seq):
    print('true')
else  :
    print('false')
