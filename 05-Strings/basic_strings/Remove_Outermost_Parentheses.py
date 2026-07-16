# Remove outermost parentheses 

def Remove_Outermost_Parentheses(str):
    
    # Initialize nesting level counter 
    level = 0

    # intialize Result string
    result = ""  

    # Traverse the string 
    for ch in str:

        if ch == '(':

            # if inside a primitive, add it 
            if level > 0:
                result += ch
            
            # increase the nesting level of "(" 
            level += 1

        elif ch == ')':

            # Decrement the nesting level
            level -= 1

            # if inside the primitive, add it 
            if level > 0:
                result += ch
           
    return result


# TC O(n)
# Sc O(1) using only few variables 
# 
# ---------------------------------------

# Intuitive approach 
"""Stack """

def Remove_Outermost_Parenthesis_(s):

    # Stack to store the valid Parenthesis
    stack = []
    result = []

    # Traversing the string 
    for char in s:
        if char == '(':
            # if stack not empty , this is an inner parenthesis
            if stack :
                result.append(char)

            # add it to stack 
            stack.append(char)

        else:
            # Char == ')' 
            # Pop from stack 
            stack.pop()

            # if stack not empty after popping, this is an inner parenthesis
            if stack:
                result.append(char)

    return "".join(result)


# TC O(n) traversing the whole string 
# SC O(N) at worst the stack would store the n/2 char 
# 
 
string = "()(()())(())"
s = "((()))"
print(Remove_Outermost_Parentheses(string))
print(Remove_Outermost_Parenthesis_(string))
print(Remove_Outermost_Parentheses(s))
print(Remove_Outermost_Parenthesis_(s))