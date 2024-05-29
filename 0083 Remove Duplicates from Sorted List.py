class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = head
        def solve(root):
            if root : 
                if root.next != None and root.val == root.next.val : 
                    root.next = root.next.next
                    solve(root)
                else:
                    solve(root.next)
        solve(head)
        return res
