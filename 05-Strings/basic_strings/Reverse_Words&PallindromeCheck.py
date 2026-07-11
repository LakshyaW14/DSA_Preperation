# Reverse words in string 

# Brute Force Approach 

def Reverse_Words_String_Brute(s):
    # list to store the result 
    words = []
    
    # Variable to store individual ch in string
    word = ""
    
    # Traversing over each words in string 
    for ch in s:
        # If not the space, append 
        if ch != " ":
            word += ch

        # If space and we have collected a word 
        elif word:
            # Add the recorded word in result 
            words.append(word)
            
            # reset the Recent word  
            word = ""

    # Add the last word, if present 
    if word:
        words.append(word)

    # Reverse the list 
    words.reverse()

    return " ".join(words)


# TC O(N)
# SC O(n) ans arr

# ----------------------------------------
# Optimal Sol 

def Reverse_Words_String_Brute(s):
    n = len(s)
    i = n -1 
    words = ""
    while ( i ):
    
        pass 

s = "hello world lakshya"

print(s[0])



s = "amazing coding skills"
# print(Reverse_Words_String_Brute(s))