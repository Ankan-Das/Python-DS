############################################################
############################################################
#Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
#For example:
#Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
#return 1->4->3->2->5->NULL.
############################################################
############################################################

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        p,q = A,A
        current = A
        value1,value2 = 1,1
        if B==C:
            return A
        while value1<B-1:
            p = p.next
            value1+=1
        while value2<C:
            q = q.next
            value2+=1
        if B==1:
            while current != q:
                temp = current
                current = current.next
                temp.next = q.next
                q.next = temp
                A = current
        else:
            while p.next != q:
                temp = p.next
                p.next = p.next.next
                temp.next = q.next
                q.next = temp
        return A
        
