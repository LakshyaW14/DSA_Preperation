#  Longest Common prefix 

# Intuition -> sort, compare first and last word of string for common prefix 

def Longest_Common_Prefix (s):

    # Edge case 
    if not s:
        return ""
    
    # to store the result
    ans =[]

    # Sort the list 
    s.sort()

    # First Word 
    first = s[0]

    # last word 
    last = s[-1]

    # Iterate for min length of first and last words
    for i in range (min( len(first), len(last))):
        # check Condition 
        if first[i] != last[i]:

            # if empty, it will return the empty string
            return "".join(ans)
        
        # If the char is equal, append
        ans.append(first[i])

    # Join the list element into single a word 
    return "".join(ans)

# TC O(n logn) sorting + O(m) comparison of string
# SC O(M) in worst case, we have to store the whole string

# ---------------------------------------

string = ["flower", "flow", "flight"]
print(Longest_Common_Prefix(string))