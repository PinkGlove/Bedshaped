from collections import defaultdict
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.cnt = defaultdict(int)
        self.queue = deque()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        self.cnt[value] += 1
        if self.cnt[value] <= 1:
            self.queue.append(value)
        while self.queue and self.cnt[self.queue[0]] > 1:
            self.queue.popleft()
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)