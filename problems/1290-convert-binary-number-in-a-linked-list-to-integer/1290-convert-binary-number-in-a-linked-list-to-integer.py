# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = head
        c=0
        while n:
            c+=1
            n = n.next
        d=0
        n = head
        for i in range(c-1,-1,-1):
            d+=n.val * (2**i)
            n = n.next
        return d