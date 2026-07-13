# Largest odd number in a string 

# Intuition -> Should not have a leading zero , iterate backwards find first odd number and check for no leading zeroes
# 

def Largest_Odd_Num(s):
    n = len(s)

    # Iterating from back of string 
    i = n-1
    
    # ending Idx of odd number 
    end = -1 
    while ( i >= 0):
        if ( int(s[i]) % 2 ) == 1:
            end = i
            break 
        # if not a odd num, move backwards 
        i -= 1

    # skipping any leading zero 
    start = 0
    while ( start <= end) and (s[start]) == '0':
        start += 1

    # Slicing -> Return the substring
    return s[start : end + 1]


# TC O(N) loop runs once through the string of length n 
# SC O(1) Constant amount of extra space 

# --------------------------------------------------

s = "0214638"
s1 = "000002435644788"
print(Largest_Odd_Num(s))
print(Largest_Odd_Num(s1))

