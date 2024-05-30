class Solution:
    def removeElement(self, nums, val):
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index

nums_example = [3, 2, 2, 3]
val_example = 3
solution = Solution()
k = solution.removeElement(nums_example, val_example)

k, nums_example  
