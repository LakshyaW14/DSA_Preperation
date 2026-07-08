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


# Optimal Sol 
"""Using Merge Sort """


def Merge (arr, low , mid, high):
    # Temp arr to store arr elements 
    temp = []

    # Count inversion Variable
    count = 0

    # Intialize pointers 
    left = low
    right = mid + 1

    # Iterate 
    while ( left <= mid ) and ( right <= high):
        
        # Leftmost ele is smaller 
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            # increment 
            left += 1

        else:
            temp.append(arr[right])
            right += 1 
            # Inversion Condition 
            # a[left] > a[right]

            count += ( mid -left + 1)

    # Copy remaining elements of left half 
    while ( left <= mid):
        temp.append(arr[left])
        left += 1

    # Copy remaining ele of right half 
    while ( right <= high):
        temp.append (arr[right])
        right += 1 

    # Copy Back to Original array 
    for i in range (low , high+1):
        arr[i] = temp[i - low]

    # Return the Inversion Count 
    return count


def Merge_Sort (arr, low , high):
    # Variable to count Inversion
    count = 0

    if low >= high:
        return count
    
    # Mid of arr 
    mid = ( low + high)//2

    #   Divide in Merge Sort 

    # count Inversion in left half 
    count += Merge_Sort(arr,low , mid )

    # count Inversion in right half 
    count += Merge_Sort(arr, mid + 1, high)

    # Merge 
    # Count inversion during merge 
    count += Merge(arr, low, mid, high)

    return count 

def Count_Inversion_Optimal (arr):
    return Merge_Sort(arr, 0, len(arr)-1)


# TC O(nlogn)  based in merge sort 
# Sc O(n) Temp arr storing the arr elements 
# ----------------------------------------- 

nums = [5,4,3,2,1 ] # 10
nums2 = [5,3,2,1,4] # 7
print ( Count_Inversion_Brute(nums))
print ( Count_Inversion_Brute(nums2))

print ( Count_Inversion_Optimal(nums))
print ( Count_Inversion_Optimal(nums2))