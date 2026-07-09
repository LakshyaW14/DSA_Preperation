# largest Sub array with sum zero 

# Brute Force 

def Largest_Subarr_Sum_Zero_Brute(arr):
    # variable to store the max length of subarr
    max_length = 0

    n = len(arr)

    # First loop 
    for i in range (n):
        # Sum var to store the sum of ele
        curr_sum = 0
        # Second Loop 
        for j in range (i, n):
            # add every element 
            curr_sum += arr[j]

            # if its equal, check it's length 
            if curr_sum == 0:
                # if present length is greater than previous ones, update 
                if ( j -i +1) > max_length:
                    max_length = j - i + 1
            
    return max_length

# TC O(n^2) Two nested loop 
# Sc O(1)

#--------------------------------------------

# Optimal Sol 
""" Prefix Sum """

def Largest_Subarr_Sum_Zero_Optimal (arr):
    # Max length so far 
    max_length = 0

    # Running Prefix sum 
    pre_sum = 0

    # Hash prefix sum -> first index seen   
    mp = {}

    # iterating over arr 
    for i, num in enumerate (arr) :
        # update prefix sum 
        pre_sum += num 

        # If sum is 0, subarr ( 0 -> i) has zero sum 
        if pre_sum == 0:

            # Update 
            max_length = i + 1 

        # IF not, check if it seen before
        else:
            # When seen, zero-sum segment between ( previous index + 1 and i )
            if pre_sum in mp:
                # Maximum length 
                max_length = max ( max_length , i - mp[pre_sum] )

            # first time seeing the sum, add it to map 
            else:
                # Record index 
                mp[pre_sum] = i

    # Return best length 
    return max_length


# TC O(n)
# SC O(n) 
#------------------------------



arr = [ 15 , -2, 2, -8, 1, 7, 10, 23 ]

print(Largest_Subarr_Sum_Zero_Brute(arr))
print(Largest_Subarr_Sum_Zero_Optimal(arr))