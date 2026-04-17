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

nums = [-1,0,1,2,-1,-4]
print(Three_sum_2(nums))