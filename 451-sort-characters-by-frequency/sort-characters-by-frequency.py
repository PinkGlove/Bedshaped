class Solution:
    def frequencySort(self, s: str) -> str:
        res = []
        cnt = Counter(s)
        tmp = []
        for k, v in cnt.items():
            heapq.heappush(tmp, (-v, k))
        while tmp:
            v, k = heapq.heappop(tmp)
            for _ in range(-v):
                res.append(k)
        return "".join(res)