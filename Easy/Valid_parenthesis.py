# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

#Brute force 
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s :
            s = s.replace('()','')
            s = s.replace('{}','')
            s = s.replace('[]','')
        return s==''
        

#optimized
class Solution:
    def isValid(self,s: str) -> bool: 
        stack=[]
        closetoOpen = { ")" : "(", "]" : "[", "}" : "{" }    # maps the closing brackets to opening  so we can check if they are in proper order
                     

        for c in s:
            if c in closetoOpen:
                if stack and stack[-1] == closetoOpen[c]: # all the open brackets go in stack first so it shouldnt be empty and if closing one comes we check the if it matches with its open one which should be the last inserted in stack 
                    stack.pop()                           # if its true we clear a perfect () or {} or [] so we pop the open from stack and check for next 
                else: 
                    return False                 
            else :
                stack.append(c)
                                     # if stack is empty or its not a pair we add the char to stack 
        return True if not stack else False
        
