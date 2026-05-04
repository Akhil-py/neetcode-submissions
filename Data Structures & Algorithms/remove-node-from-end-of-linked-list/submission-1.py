# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        i = 0
        length = 0

        parse = head
        while parse:
            parse = parse.next
            length += 1

        remove_index = length - n

        while curr:
            nxt = curr.next
            if i == remove_index:
                if prev is None:
                    curr.next = None
                    head = nxt
                else:
                    prev.next = nxt
                    curr.next = None
                return head
            prev = curr
            curr = curr.next
            i += 1

            