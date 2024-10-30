class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lis = []
        lis_len = [1] * len(nums)
        for i_nums, num in enumerate(nums):
            i = bisect_left(lis, num)
            if i == len(lis):
                lis.append(num)
            else:
                lis[i] = num
            lis_len[i_nums] = len(lis)
        lds = []
        lds_len = [1] * len(nums)
        for i_nums, num in enumerate(nums[::-1]):
            i = bisect_left(lds, num)
            if i == len(lds):
                lds.append(num)
            else:
                lds[i] = num
            lds_len[i_nums] = len(lds)
        lds_len = lds_len[::-1]
        res = len(nums)
        print(lis_len)
        print(lds_len)
        for i in range(len(nums)):
            if lis_len[i] > 1 and lds_len[i] > 1:
                cnt = i + 1 - lis_len[i] + len(nums) - i - lds_len[i]
                res = min(res, cnt)
        return res
