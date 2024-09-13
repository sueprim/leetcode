# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = []
        dic = {}
        while head : 
            if head.val in dic : 
                dic[head.val] = 2
            else : 
                dic[head.val] = 1
            head = head.next
        for k in dic:
            if dic[k] == 2 : 
                continue
            else : 
                temp.append(k)
        temp.sort()
        res = ListNode()
        finall = res
        for i in range(len(temp)):
            res.next = ListNode(temp[i])
            res = res.next
        return finall.next
