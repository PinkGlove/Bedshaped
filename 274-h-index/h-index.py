class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(h):
            cnt = 0
            for citation in citations:
                if citation >= h:
                    cnt += 1
            return cnt >= h
        l, r = 0, max(citations)
        while l < r:
            mid = l + r + 1 >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l