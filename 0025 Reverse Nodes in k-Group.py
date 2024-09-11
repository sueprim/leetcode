# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 : 
            return head
        node = ListNode()
        dq = []
        res = []
        while head : 
            dq.append(head.val)
            head = head.next
        idx = 0
        while idx+k <= len(dq) : 
            temp = dq[idx:idx+ k]
            temp.reverse()
            res += temp
            idx = idx + k
        res += dq[idx:]
        temp = node
        for i in range(len(res)):
            temp.next = ListNode(res[i])
            temp = temp.next
        return node.next
