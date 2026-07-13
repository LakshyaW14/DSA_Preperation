# Isomorphic String

# Intuition ->
# if ch in s can be replaced to get t 
# no two char may map to same char 
# Char may map to itself 

# s = "paper " t = " title "
# p->t a->i p->t e->l r->e


def Isomorphic_String(s,t):
    # arr to track last seen position of char 
    m1 = [0] *256
    m2 = [0] * 256

    # length 
    n= len(s)

    # Loop through each char in both string
    for i in range(n):
        # Return False if last seen position don't match 
        if m1[ord(s[i])] != m2[ord(t[i])]:
            return False
        
        # Update Last seen position with current index + 1
        m1[ord(s[i])] = i + 1
        m2 [ord(t[i])] = i + 1

    # Return True if no inconsistencies found 
    return True

# TC O(n) 
# SC O(1) the space used by arr is constant, regardless of the input size

# ---------------------------------

s = "paper"
t = "title"

s1 = "foo"
t1 = "bar"

print(Isomorphic_String(s,t))
print(Isomorphic_String(s1,t1))