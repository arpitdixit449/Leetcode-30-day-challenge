'''
Problem Statement -> Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
                       push(x) -- Push element x onto stack.
                       pop() -- Removes the element on top of the stack.
                       top() -- Get the top element.
                       getMin() -- Retrieve the minimum element in the stack.
    
'''

#Solution : Time O(1)[All Operations], Space O(n)

class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        curr = x
        if len(self.minstack):
            curr = min(x,self.minstack[-1])
        self.minstack.append(curr)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minstack):
            return self.minstack[-1]
