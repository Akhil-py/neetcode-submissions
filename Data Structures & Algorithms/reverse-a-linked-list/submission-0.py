# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = head
        curr = head.next
        nxt = head.next.next

        prev.next = None

        while nxt is not None:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
            print(curr.val)
        curr.next = prev
        
        return curr