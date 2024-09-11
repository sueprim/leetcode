class Solution(object):
    def numJewelsInStones(self, J, S):
        J_count = 0
    
        for x in S:
            if x in J:
                J_count += 1

        return J_count
