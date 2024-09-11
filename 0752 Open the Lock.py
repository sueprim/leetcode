class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadset = set(deadends)
        v = set('0000')
        dq = deque([('0000',0)])
        
        while dq : 
            slot,counting = dq.popleft()
            if slot == target : 
                return counting
            elif slot in deadset : 
                continue
            for i in range(4) : 
                digit = int(slot[i])
                for move in [-1,1]:
                    newdigit = (digit + move)%10
                    newslot = slot[:i] + str(newdigit) + slot[i+1:]
                    if newslot not in v:
                        v.add(newslot)
                        dq.append((newslot,counting+1))
        return -1 
