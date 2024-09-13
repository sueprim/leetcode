# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = head
        if head == None or head.next == None : 
            return res
        curr = head
        fast = head.next
        while True:
            curr.val, fast.val = fast.val, curr.val
            if curr.next == None or curr.next.next == None or fast.next == None or fast.next.next ==None:
                break
            curr = curr.next.next
            fast = fast.next.next
        return res
