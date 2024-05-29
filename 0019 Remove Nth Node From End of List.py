class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        endNode = head 
        length = 1
        
        while endNode.next: 
            endNode = endNode.next
            length += 1
            
        if length == 1 and n == 1: 
            head.val = ''
            return head 
            
        if length - n == 0: 
            return head.next 
        nodeBefore = head
        for _ in range(length - n - 1):
            nodeBefore = nodeBefore.next        
        nodeBefore.next = nodeBefore.next.next
        
        return head
