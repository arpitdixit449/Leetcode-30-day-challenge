'''
Problem Statement -> Given two strings S and T, return if they are equal when both are 
                     typed into empty text editors. # means a backspace character.
                     
Example 1 -> Input: S = "ab#c", T = "ad#c"
             Output: true
             Explanation: Both S and T become "ac".
             
Example 2 -> Input: S = "ab##", T = "c#d#"
             Output: true
             Explanation: Both S and T become "".
'''

#Solution - Using Stack : Time O(n), Space O(n)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1 = self.back_string(S)
        s2 = self.back_string(T)
        return s1 == s2
    
    def back_string(self, string):
        stack = []
        for i in string:
            if len(stack) >0 and i == "#":
                stack.pop()
            elif i != "#":
                stack.append(i)
        return "".join(stack)
