# Nth root of the Number 

# Brute Force 

def nth_Root_Brute(num, exp):

    for i in range (num):
        if pow(i, exp) == num:
            return i
        elif pow(i, exp) > num:
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

        if pow(mid, exp) == num:
            return mid
        elif pow(mid, exp ) > num:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# TC O( logn)
# SC O(1)

#-------------------------
print(Nth_Root_Optimal(num=69, exp=4))