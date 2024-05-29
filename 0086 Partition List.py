class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        less_than_x = ListNode(0)
        equal_or_bigger_than_x = ListNode(0)

        l, e = less_than_x, equal_or_bigger_than_x

        if head.val < x:
            l.next = ListNode(head.val)
            l = l.next
        else:
            e.next = ListNode(head.val)
            e = e.next

        while head.next:
            head = head.next
            if head.val < x:
                l.next = ListNode(head.val)
                l = l.next
            else:
                e.next = ListNode(head.val)
                e = e.next
                
        l.next = equal_or_bigger_than_x.next
        return less_than_x.next
