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
