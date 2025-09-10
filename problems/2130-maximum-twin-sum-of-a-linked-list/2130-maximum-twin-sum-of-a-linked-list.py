# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        m, n = 0, len(l)
        for i in range(n // 2):
            m = max(m, l[i] + l[n - i - 1])
        return m