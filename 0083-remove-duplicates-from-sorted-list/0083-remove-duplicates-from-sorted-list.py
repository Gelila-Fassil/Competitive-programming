# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = head
        # while curr and:
        #     if curr.val == curr.next.val:
        #         curr.next = curr.next.next
        #         curr = curr.next
        #     else:
        #         curr = curr.next
        # return head
        




















        if not head:
            return head
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
                
        return head