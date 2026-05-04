# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        seen = deque()
        curr = head

        while curr:
            seen.append(curr)
            curr = curr.next

        prev = seen.popleft()
        while seen:
            node = seen.pop() 
            prev.next = node
            prev = node
            node.next = None
            if seen:
                node = seen.popleft()
                prev.next = node
                prev = node
                node.next = None
        
