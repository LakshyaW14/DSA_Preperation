# Find the Smallest Divisor within a given Threshold

import math
# Brute Approach 
# Intuition -> low = 1 , high = max(Arr)

def Func(arr, t):
    count = 0
    for i in range (len(arr)):
        count += math.ceil(arr[i]/t)
    return count

def Find_Smallest_Divisor(arr, Threshold ):

    for i in range ( 1, max(arr) + 1):
        if Func(arr, i) <= Threshold:
            return i
    return -1

# TC O(n) x O(max(Arr))
# SC O(1)

#-------------------------------------

arr = [ 1,2,5,9]
print(Find_Smallest_Divisor(arr,Threshold=6))