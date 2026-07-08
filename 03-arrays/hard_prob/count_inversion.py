# Count inversion 
# Brute force 
# Intuition -> i < j  a[i] > a[j]

def Count_Inversion_Brute(arr):
    # count variable
    count = 0

    # First loop 
    for i in range (len(arr)):
        # Second loop 
        for j in range ( i+1, len(arr)):

            # Inversion Condition 
            if arr[i] > arr[j]:
                count += 1 
    return count 

# Tc O( n ^2) nested loop , as every pair is checked 
# Sc O( 1) 

# ------------------

nums = [5,4,3,2,1 ] # 10
nums2 = [5,3,2,1,4] # 7
print ( Count_Inversion_Brute(nums))
print ( Count_Inversion_Brute(nums2))