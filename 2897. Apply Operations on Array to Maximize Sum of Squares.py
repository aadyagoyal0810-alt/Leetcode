class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        cnt = [0] * 31
        for n in nums:
            for b in range(31):
                if n >> b & 1:
                    cnt[b] += 1

        ans = 0
        for _ in range(k):
            cur = 0
            for b in range(31):
                if cnt[b] > 0:
                    cur |= (1 << b)
                    cnt[b] -= 1
            ans = (ans + cur * cur) % MOD
        return ans
        
