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



arr = [ 15 , -2, 2, -8, 1, 7, 10, 23 ]

print(Largest_Subarr_Sum_Zero_Brute(arr))