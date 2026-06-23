# Find Square Root of a num 

# Brute Force Approach

def Brute_Sqrt(num):
    ans = 0
    for i in range(num):
        if i*i <= num:
            ans = i
        else:
            break
    return ans 

# TC O(n)
# SC O(1)

#------------------------------------

# optimal Approach 

def Sqrt_Optimal (num):

    low = 1
    high = num

    while ( low <= high):
        mid = ( low + high)//2
        # Left Half eliminated, ans in right
        if (mid * mid) <= num:
            low = mid + 1
        
        # Ans in Left Half 
        else:
            high = mid - 1

    return high

# TC O(logn)
# SC O(1)


print(Brute_Sqrt(num=28))
print(Sqrt_Optimal(num=28))