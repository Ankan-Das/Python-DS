######################################################
######################################################
#Sort a linked list using insertion sort.
######################################################
######################################################
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        x = 0
        value = A.val
        current = A
        first = A
        if A.next is None:
            return A
        while current.next is not None:
            p = A
            if current.next.val<current.val:
                x = current.next.val
                if x<p.val:
                    temp = current.next
                    current.next = current.next.next
                    temp.next = A
                    A = temp
                else:
                    while True:
                        if p.next.val<x:
                            p = p.next
                        else:
                            temp = current.next
                            current.next = current.next.next
                            temp.next = p.next
                            p.next = temp
                            break
            
            else:
                current = current.next
        return A
