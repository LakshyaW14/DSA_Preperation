# 3 Sum : Find triplets that add up to a zero

def Three_Sum(nums):
   
   # Store unique elements
   st =set()

   # first loop for first element
   for i in range (len(nums)):
      # second loop for second element
        for j in range (i, len(nums)):
            # third loop for third element 
            for k in range (j, len(nums)):    
                    # if triplet sum is zero
                if ( nums[i] + nums[j] + nums[k] ) == 0:
                    # Store the triplets to avoid duplicates
                    triplet = tuple(sorted([ nums[i], nums[j], nums[k] ]))
                    st.add(triplet) 

    # convert set to list of lists
        return [ list(triplet) for triplet in st]                    

#Time Complexity: O(N3 * log(no. of unique triplets)), where N = size of the array.
# Space Complexity: O(2 * no. of the unique triplets) as we are using a set data structure and a list to store the triplets.

#--------------------------------------------------

# Better Approach 
def Three_sum_2(nums):
    # set -> store unique elements
    res =set()

    # first loop for first element
    for i in range (len(nums)):
        # set to store the seen elements in this iteration 
        hashset = set()

        # Second loop for second element 
        for j in range (i, len(nums)):
            third = -(nums[i] + nums[j]) 

            if third in hashset :
                triplet = tuple(sorted([nums[i], nums[j], third]))
                res.add(triplet)

            # add current elemant 
            hashset.add(nums[j])
        
    return [ list(triplet) for triplet in res ]



# Time Complexity: O(N2 * log(no. of unique triplets)),
# as we are mainly using 3 nested loops. And inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. \
#     But we are not considering the time complexity of sorting as we are just sorting 3 elements every time.

# Space Complexity: O(2 * no. of the unique triplets) + O(N) as we are using a set data structure and a list to store the triplets and \
#     extra O(N) for storing the array elements in another set.


#-------------------------------------------------------------
# optimal Approach 

def Three_Sum_3(nums):
    # Sort the array 
    nums.sort()

    # Store the final Result 
    res =[]

    # First loop for first element 
    for i in range (len(nums)):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Two pointers 
        left , right = i+1, len(nums)-1

        # Find pairs for nums[i]
        while left < right :
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                left +=1
                right -=1

                # Skip duplicates for left 
                while left < right and  nums[left] == nums[left -1]:
                    left +=1
                while left < right and nums[right] == nums[right +1]:
                    right -=1
            elif total < 0:
                left +=1
            else:
                right -=1
    return res 
    

# Time Complexity: O(NlogN)+O(N2), as The pointer i, is running for approximately N times. And both the pointers j and k combined \
#     can run for approximately N times including the operation of skipping duplicates. So the total time complexity will be O(N2). 

# Space Complexity: O(no. of quadruplets), This space is only used to store the answer.\
#       We are not using any extra space to solve this problem. So, from that perspective, space complexity can be written as O(1).


nums = [-1,0,1,2,-1,-4]
print(Three_Sum_3(nums))