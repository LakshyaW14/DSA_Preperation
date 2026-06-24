# Nth root of the Number 

# Brute Force 

def nth_Root_Brute(num, exp):
    # Loop from 1 to m
    for i in range (num):
        # compute i^n
        power = i ** exp
    
    # if equals to m, return i 
        if power == num:
            return i
    
    # If Exceeds m, break 
        if power > num:
            break 

    return -1

# TC O( n x logn ) if using the pow function O( n x m) if using loop for pow calc
# Sc O(1)

#-----------------------

# Optimal Sol 

def Nth_Root_Optimal ( num, exp):

    low = 1
    high = num

    while ( low <= high):
        mid = ( low + high) // 2

        # Store result of mid ^ exp
        ans =1
        for _ in range (exp):
            ans *= mid 
            if ans > num:
                break 
        # If mid^n equals to num 
        if ans == num:
            return mid
        
        # if mid^n greater than num 
        elif ans > num:
            high = mid - 1
        # if mid ^n is smaller 
        else:
            low = mid + 1
    return -1

# TC O( logn)
# SC O(1)

#-------------------------
print(Nth_Root_Optimal(num=27, exp=3))