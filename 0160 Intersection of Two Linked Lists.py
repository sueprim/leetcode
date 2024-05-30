class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        aMap = set()
        
        while headA: 
            aMap.add(headA) 
            headA = headA.next
        
        while headB:
            if headB in aMap: 
                return headB
            else:
                headB = headB.next
        return None
