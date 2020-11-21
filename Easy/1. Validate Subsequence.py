#O(n) -> Time | O(1) -> Space
# Steps :
# 1) Initialize i and j as 0 where i will iterate through arr
#    and j will iterate through seq
# 2) If the first match is found, then only we increment i and j
#    else we increment i as we move fwd in arr.
# 3) c increments for every match. If c equals length of seq, print true.
def validateSubsequence(arr, seq):
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
