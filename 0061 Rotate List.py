# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None : 
            return None
        temp = deque()
        res = head
        while head : 
            temp.append(head.val)
            head= head.next
        k = k % len(temp)
        finall = res
        temp.rotate(k)
        for i in range(len(temp)) : 
            res.val = temp[i]
            if i != len(temp)-1 : 
                res.next = ListNode()   
            res = res.next
            
        
        return finall
