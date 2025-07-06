# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            temp= slow.next
            slow.next = prev
            prev = slow
            slow= temp

        # left, right= head, prev
        # while right is not None:
        #     temp1 = left.next
        #     temp2 = right
        #     left.next = temp2
        #     right = temp1
        #     left, right = left.next, right.next

        left, right = head, prev
        while right and left:
            temp1 = left.next
            temp2 = right.next

            left.next = right
            right.next = temp1

            left = temp1
            right = temp2

            if not right or not left:
                break

        if left:
            left.next = None        