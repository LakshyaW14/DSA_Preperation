# find the majority Element ( > n/ 3) 


# Brute Force 
def Majority_Element_two (arr):
    ans = []
    n = len(arr)

    # First loop 
    for i in range (n):
        # Variable to store the frequency 
        count = 0
        # skip duplicates 
        if arr[i] in ans :
            continue

        for j in range (n ):
            if arr[i] == arr[j]:
                count += 1
        
        if count > ( n//3 ):
            ans.append(arr[i])

        # Early break -> at most only two elements 
        if len(ans) == 2 :
            break 
    return ans 

# TC O(n^2) nested loop 
# SC O(1)

# ----------------------------------------------

# Better approach 
""" Hashing"""
# intuition -> ( number, count )

def Majority_Element_two_Better (arr):
    hash_mp = {}
    ans = []
    n = len(arr)
    
    # mini times the number should appear
    mini = ( n //3 + 1 )
    for num in arr:
        # Storing the element with it's occurrence
        hash_mp[num] = hash_mp.get(num, 0) + 1

        # Check Condition 
        if hash_mp[num] == mini:
            ans.append(num)
        
        # Early break 
        if len(ans) == 2:
            break 

    return ans

# TC O(n) going through every ele in arr 
# Sc O(n) at Worst need to store every ele 

# -----------------------------------------

# Optimal Sol 
""" Moore's Vooting Algo """
# Intuition -> Look for dominating Cancle 

def Majority_Element_two_Optimal (arr):
    # At max only two elements are present that are in majority ( > n// 3)
    n = len(arr)

    # To store the result 
    ans =[]

    # Intialize count variables for ele1 and ele2
    count1 , count2 = 0, 0

    # Intialize ele variables
    ele1, ele2 = 0, 0

    # Finding the Possible candidate by Booye moore voting algo 
     
    for num in arr :
        # First Element 
        if ( count1 == 0) and ( num != ele2 ):
            count1 = 1
            ele1 = num 
        
        elif ( count2 == 0) and ( num != ele1):
            count2 = 1
            ele2 = num

        # if similar num occurs 
        elif num == ele1 :
            count1 += 1
        elif num == ele2 :
            count2 += 1

        # if not similar 
        else:
            count1 -= 1
            count2 -= 1

    # Validate the Candidates by counting occurence in arr
    # Reset count 
    count1 , count2 = 0, 0
    for num in arr :
        if num == ele1:
            count1 += 1
        if num == ele2:
            count2 += 1
    # minimum Count required to be majority ele 
    mini = ( n//3 +1)

    if count1 >= mini:
        ans.append(ele1)

        # avoid adding duplicates if ele1 == ele2
    if count2 >= mini and ele1 != ele2 :
        ans.append(ele2)

    # Sort if neccessary
    # ans.sort()
    
    return ans


# TC O(n) Traversing the arr twice, once to find possible candidate and once to validate them 

# SC O(1) constant amount of time for  counters and candidate ele 

# --------------------------------------------------------

nums = [1, 2, 1, 1, 3,2, 2]  
print(Majority_Element_two(nums))
print(Majority_Element_two_Better(nums))
print(Majority_Element_two_Optimal(nums))
