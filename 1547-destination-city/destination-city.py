class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = defaultdict(str)
        for a, b in paths:
            d[a] = b
        start = paths[0][0]
        while start in d:
            start = d[start]
        return start