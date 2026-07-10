# Reverse pairs 
# Intuition -> i < j and a[i] > 2 * a[j]

# Brute Force Approach 
def Reverse_Pairs_Brute(arr):

    count = 0
    # First loop 
    for i in range (len(arr)):
        # Second Loop 
        for j in range ( i+1, len(arr)):
            # Reverse Pairs condition 
            if arr[i] > 2 * arr[j]:
                count += 1

    return count

# TC O(n^2) nested Loop 
# SC O(1)

#------------------------------
nums = [1,3,2,3,1]
print(Reverse_Pairs_Brute(nums))