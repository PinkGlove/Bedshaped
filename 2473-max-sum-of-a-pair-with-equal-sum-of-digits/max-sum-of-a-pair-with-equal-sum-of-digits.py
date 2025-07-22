import heapq

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for num in nums:
            digits_sum = 0
            tmp = num
            while tmp > 0:
                digits_sum += tmp % 10
                tmp //= 10
            heapq.heappush(d[digits_sum], -num)
        res = -1
        for v in d.values():
            if len(v) >= 2:
                res = max(res, -heapq.heappop(v) - heapq.heappop(v))
        return res
                
