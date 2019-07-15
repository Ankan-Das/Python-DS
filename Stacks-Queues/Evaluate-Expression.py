############################################################
############################################################
#Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
#Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
#Examples:
#
#  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
###########################################################
###########################################################

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        value = A[0]
        i=0
        length = len(A)
        while i<length:
            if A[i]=="+":
                value = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(value)
            elif A[i]=="-":
                value = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(value)
            elif A[i]=="*":
                value = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(value)
            elif A[i]=="/":
                value = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(value)
            else:
                stack.append(int(A[i],10))
            i+=1
        return int(value)
