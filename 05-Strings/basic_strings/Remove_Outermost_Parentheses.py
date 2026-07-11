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
 
string = "()(()())(())"
s = "((()))"
print(Remove_Outermost_Parentheses(string))
print(Remove_Outermost_Parentheses(s))