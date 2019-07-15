############################################################
############################################################
#Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
#
#More formally,
#
#G[i] for an element A[i] = an element A[j] such that 
#    j is maximum possible AND 
#    j < i AND
#    A[j] < A[i]
#Elements for which no smaller element exist, consider next smaller element as -1.
#
#Example:
#
#Input : A : [4, 5, 2, 10, 8]
#Return : [-1, 4, -1, 2, 2]
#
#Example 2:
#
#Input : A : [3, 2, 1]
#Return : [-1, -1, -1]
###########################################################
###########################################################

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack = []
        listed = []
        length = len(A)
        i=0
        while i<length:
            while len(stack):
                if stack[-1]<A[i]:
                    listed.append(stack[-1])
                    stack.append(A[i])
                    break
                else:
                    stack.pop()
            if not len(stack):
                stack.append(A[i])
                listed.append(-1)
            i+=1
        return listed
