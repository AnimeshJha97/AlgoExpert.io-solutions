# Given a special array which can contain integers as well as list which can
# further store list or integer and so on.
# We need to find the product Sum of the array such that the sum of array is
# multiplied by its respective depth.

# Example: [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
# Here, element 5,2,3 are present at depth=1
# elements 7,-1 are at depth 2
# Similarly 6 at depth 2 and
# -13,8 at depth 3

# Calculation : 
# {5 + 2 + [(7+(-1)) * 2] + 3 + [_[6 + (-13+8)*3 + 4] * 2_]} * 1 == 12

# So, for every list occurence, we need to calculate the sum of the list and
# then multiply it by the depth of that list

def productSum(array, mult = 1):
    sum = 0
    for ele in array:
        if type(ele) is list:
            sum += productSum(ele, mult+1)
        else:
            sum += ele
    return sum * mult



ar = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(ar))
