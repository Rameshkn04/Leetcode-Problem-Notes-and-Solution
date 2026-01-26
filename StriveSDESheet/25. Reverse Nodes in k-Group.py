# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
         
        if count == k:
            prev = self.reverseKGroup(node,k)
            current = head
            while count > 0:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
                count -= 1
            return prev
        return head
