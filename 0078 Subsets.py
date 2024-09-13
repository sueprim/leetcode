class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answers = []
        q = deque([(0, [])])

        while q:
            idx, cur = q.popleft()

            answers.append(cur[:])

            for i in range(idx, len(nums)):
                q.append((i + 1, cur  + [nums[i]]))

        return answers
