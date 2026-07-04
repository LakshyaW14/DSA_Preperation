# Find the Missing and Repeating number 

# Brute Force Approach 

def Find_Missing_Repeating(arr):
    # Intialize variable 
    repeating, missing = -1 , -1
    
    # Generating Num from 1 to n
    for i in range (1, len(arr) + 1 ):
        count = 0 
        
        # Iterating over the arr 
        for j in range (len(arr)):
            if arr[j] == i:
                count += 1
        # Repeating Condition 
        if count == 2:
            repeating = i
        
        # Missing condition 
        elif count == 0:
            missing = i

        # early break 
        if ( repeating != -1) and ( missing != -1):
            break

    return [repeating, missing ]

# Time Complexity O( n^2) where n is the size of array, and nested Loop 
# SC O(1) using constant amount of space for Var, regardless of input size 

# ---------------------------------------------

# Better - > hashing

def Find_Missing_Repeating_Better(arr):
    n = len(arr)
    repeating, missing = -1 , -1


    # Intialize a hash arr for counting occurrence 
    hash_arr = [0] * (n+1)

    # 
    for num in arr:
        hash_arr[num] += 1
    
    for i in range (1, n+1):
        if hash_arr[i] == 2:
            repeating = i

        elif hash_arr[i] == 0:
            missing = i

        # early break 
        if ( repeating != -1) and ( missing != -1):
            break

    return [ repeating, missing]
    

# TC O(2n)
# SC O(n) ae we are using a additional Hash arr 

# -----------------------------

# 1st Optimal sol 
# Using Math 

def Find_Missing_Repeating_Optimal1(arr):
    n = len(arr)

    # Sum of first N natural number 
    sn = (n*(n+1)) //2
    # sum of square of n natural number 
    sn2 = ( (n) *(n+1)*(2*n+1))//6

    s, s2 = 0, 0
    for num in arr:
        s += num
        s2 += num ** 2

    # Compute the difference val x - y
    val1 = s - sn

    # Compute the x^2 - y^2
    val2 = s2 - sn2

    # Calculate x + y using x^2 - y^2 // x - y
    val2 = val2 // val1
    
    """ Calculate X and Y from X + Y and X - Y
        X = ((X + Y) + (X - Y)) / 2
        Y = X - (X - Y) """
    
    x= ( val1 + val2)//2
    y = x - val1

    return [ x, y]

# TC O(n) loop to calculate the sum and square of sum 
# SC O(1) constant amount of space for variables 

# -----------------------------------------


# Optimal Sol 2 
# Using bit manipulation and xor 

# Intuition ->
# 1. xor of arr int and n natural numbers
# 2. Find the differentiating Bit of the Xor Num 
# 3. put them into two parts  

def Find_Missing_Repeating_Optimal2(arr):

    # 1. xor of a[num] and n nums  -> O(n)
    n = len(arr)
    xr = 0
    for i in range (n):
        xr ^= arr[i]    # xor of all ele in Arr  
        xr ^= i + 1     # xor of numbers from 1 to n 

    # 2. Differentiating Bit  ( Get the Rightmost set bit in xr )
    # e.g. xr = 4 in Bin 100 
    # so 100 & ( 001 -> 010 -> 100) 
    # 100 & 100 gives 1 at 2nd Bit i.e 2nd Bit is differentiating Bit 

    Bit_No = 0          # O(1) using xr & -xr or O(logn ) if scanning Bits 
    while True :
        
        if xr & ( (1 << Bit_No) ):
            break
        Bit_No += 1
    
    # Or Advanced way 
    # Bit_Num = xr & ~(xr - 1 )

    # 3. group numbers -> Zero Club and one Club  -> O(n)
    one, zero = 0, 0
    # Dividing Array Into Two Groups 
    for i in range (n):
        if ( arr[i] )  & (1<< Bit_No ):
        # or arr[i] & Bitnum :
            # one part club
            one ^= arr[i] 
        else:
            # Zero Club 
            zero ^= arr[i]
    # Dividing numbers into Two Groups
    for i in range (1, n+1):
        if i & Bit_No :
            one ^= i
        else: 
            zero ^= i
    

# Manual Check -> Determine Which is Repeating and Missing  O(n)
    count = 0
    for i in range (n):
        if arr[i] == zero :
            count += 1
    if count == 2:
        return ( zero , one )  # Repeating , missing
    else:
        return ( one , zero )

# TC  O(n)
# SC O(1)

# -------------------------------------


arr = [ 2,3,4,1,1,6]
print(Find_Missing_Repeating(arr))
print(Find_Missing_Repeating_Better(arr))
print(Find_Missing_Repeating_Optimal1(arr))
print(Find_Missing_Repeating_Optimal2(arr))
