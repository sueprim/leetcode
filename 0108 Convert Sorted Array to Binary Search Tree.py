class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        def dfs(left, right):
            if left>right:
                return

            
            mid=(left+right+1)//2
            
            root=TreeNode(nums[mid])
            
            root.left=dfs(left, mid-1)
            root.right=dfs(mid+1, right)
            
            return root
        
        return dfs(0, len(nums)-1)
