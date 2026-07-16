# Reverse words in string 

# Brute Force Approach 
# String are immutable in py

# Intuition -> Extract word -> reverse
# list -> join 

def Reverse_Words_String_Better(s):
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

# Intuition  -> Move from right to left, build the output directly 

def Reverse_Words_String_Brute(s):
    n = len(s)

    # result String
    Res = ""

    # Intialize the pointer, starting from end 
    i = n -1
    
    # Each char is visited at most twice
    # 1. once while skipping spaces 
    # 2. once while scanning a word 

    while i >= 0: 
        # skipping spaces 
        while i >= 0 and s[i] == " ":
            # Skip Spaces 
            i -= 1

        # If i goes out of bounds 
        if i < 0 :
            break 

        # Mark end of the word
        end = i

        # move left until space or start 
        while i>= 0 and s[i] != " ":
            i -= 1

        # Extract the word 
        word = s[ i + 1 : end +1]

        # Add space if result is not empty 
        if Res :
            Res += " "

        # append word 
        Res += word

    return Res


# TC O(n)
# SC (n)

# ----------------------------


s = "hello world lakshya"




s = "amazing coding skills"
# print(Reverse_Words_String_Brute(s))