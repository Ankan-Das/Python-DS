# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):
	    value = A
        p = []
        p.append(A.val)
        while A.next is not None:
           A = A.next
           p.append(A.val)
        y = p.copy()
        p.reverse()
        if p==y:
            return 1
        else:
            return 0
