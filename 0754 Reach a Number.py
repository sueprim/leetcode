class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        if not target: return 0
        step = 1
        total = 0
        while True:
            total += step            
            if total >= target and (total-target)%2 == 0:
                return step
            step += 1
        return -1
