class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_dic = {}

        for a in arr:
            num = remainder_dic.get(a % k, 0)
            remainder_dic[a % k] = num + 1

        for key, value in remainder_dic.items():
            if value > 0:
                pair_remainder = k - key

                if pair_remainder == key:
                    if value % 2 == 0:
                        remainder_dic[key] = 0
                        continue
                    else:
                        return False

                pair_remainder_cnt = remainder_dic.get(pair_remainder, 0)
                if pair_remainder_cnt >= value:
                    remainder_dic[pair_remainder] = pair_remainder_cnt - value
                    remainder_dic[key] = 0

        for key, value in remainder_dic.items():
            if key == 0:
                continue
            if value > 0:
                return False

        return True
