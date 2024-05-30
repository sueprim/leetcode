class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr!= None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        return prev
