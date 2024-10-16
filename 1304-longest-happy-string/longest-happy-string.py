import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heappush(heap, (-a, "a"))
        if b > 0:
            heappush(heap, (-b, "b"))
        if c > 0:
            heappush(heap, (-c, "c"))
        res = []
        while heap:
            cnt, c = heappop(heap)
            cnt = -cnt
            if len(res) >= 2 and res[-1] == c and res[-2] == c:
                if not heap:
                    break
                next_cnt, next_c= heappop(heap)
                next_cnt = -next_cnt
                res.append(next_c)
                next_cnt -= 1
                if next_cnt > 0:
                    heappush(heap, (-next_cnt, next_c))
                heappush(heap, (-cnt, c))
            else:
                cnt -= 1
                res.append(c)
                if cnt > 0:
                    heappush(heap, (-cnt, c))
        return "".join(res)
