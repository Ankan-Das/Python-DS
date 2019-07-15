############################################################
############################################################
#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#push(x) – Push element x onto stack.
#pop() – Removes the element on top of the stack.
#top() – Get the top element.
#getMin() – Retrieve the minimum element in the stack.
#Note that all the operations have to be constant time operations.
#
#Questions to ask the interviewer :
#
#Q: What should getMin() do on empty stack? 
#A: In this case, return -1.
#
#Q: What should pop do on empty stack? 
#A: In this case, nothing. 
#
#Q: What should top() do on empty stack?
#A: In this case, return -1
##########################################################
##########################################################

class MinStack:
    stack = []
    minimums = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append(x)
            self.minimums.append(x)
        else:
            self.stack.append(x)
            if x < self.minimums[-1]:
                self.minimums.append(x)
            else:
                self.minimums.append(self.minimums[-1])

    # @return nothing
    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
            self.minimums.pop()

    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack[-1]

    # @return an integer
    def getMin(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.minimums[-1]
    
    def __init__(self):
        self.stack = []
        self.minimums = []

