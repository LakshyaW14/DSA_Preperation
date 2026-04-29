# Left Rotate the Array by one (Two pointer)

def Rotate_Array(arr):
    i = 0       
    for j in range (1, len(arr)):
        arr[i], arr[j] = arr[j] , arr[i]
        i+=1
# Swapping -> not scalable for k rotations 
#---------------------------------------------------

# Brute force Approach 
def rotate_array(arr):
    first =arr[0]

    for j in range (1, len(arr)):
        arr[j-1] =arr[j]
    arr[-1] = first

    # TC O(N)
    # Sc O(1) extra space used , for implementing th algorithm O(N) 
#----------------------------------------------------

# rotate the array with k elements ( left )
# brute Force Approach 

def Rotate_k(arr,k,direction ):
    n =len(arr)
    if n == 0:
        return 
    
    # If K is larger than the size of array, e.g. k =20 , n= 7 so the roation will be ( 7 + 7 + 6 ) i.e 6 element need roatation 
    k %=n 

    if direction == " left":

        # store first ( left ) k elements 
        temp =arr[:k]

        #shift remaining elements
        for i in range (k,n):
            arr[i-k] = arr[i]

        # copy the stored elements to the end 
        for i in range (k):
            arr[n-k+i] = temp[i]


    elif direction == "right":

        # store last k elements 
        temp=arr[-k:]

        # shift the remaining elements
        for i in range (n-k-1, -1, -1):
            arr[i+k] =arr[i]

        # copy stored elements to the front
        for i in range(k):
            arr[i] = temp[i]




# TC -> O(k) + O(n-k) + O(k) = O(n+k)
# SC O(k)


#----------------------------------------------
# Optimal approach 
# In place modification 

# helper function to reverse the part of array between the indices 
def reverse ( nums, start, end):
    #  swap elements from start to end 
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start +=1
        end -=1

def RotateArray(nums, k, direction ):
    n = len(nums)

    # edge case -> no rotation 
    if n ==0 or k == 0:
        return nums 
    
    # normalize the k if larger than n
    k %= n

    if direction == "right" :
        # step 1 -> Reverse the entire array 
        reverse(nums, 0 , n-1)

        # step 2 -> Reverse first k elements 
        reverse(nums, 0, k-1)

        # step 3 -> Reverse the remaining n-k elements 
        reverse(nums, k, n-1)

    elif direction == "left":
        # step 1 -> Reverse first k element O(k)
        reverse(nums, 0, k-1)

        # step 2 -> Reverse the remaining n-k elements o(n-k)
        reverse (nums, k, n-1)

        # step 3 -> Reverse the entire array O(n)
        reverse(nums, 0, n-1)
    
    return nums

# Tc -> O(k) + O(n-k) + O(n) = O(2N)
# SC O(1)

#-----------------------------------------------------------------
    
nums=[1,2,3,4,5,6,7]
print(nums)

# RotateArray(nums,3, "left")
Rotate_k(nums, 2, "right")
print()
print(nums)
