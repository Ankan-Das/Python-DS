# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        head1 = ListNode(0)  # handle for nodes < B
        head2 = ListNode(0)  # handle for nodes >= B
        node1, node2 = head1, head2
        while A:
            if A.val < B:
                node1.next, node1, A = A, A, A.next
            else:
                node2.next, node2, A = A, A, A.next
        # Link the two lists
        node1.next = head2.next
        # Clear last pointer
        node2.next = None
        return head1.next
