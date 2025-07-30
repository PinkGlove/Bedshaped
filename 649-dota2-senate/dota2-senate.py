class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        cnt = Counter(senate)
        curr_cnt = {'R': 0, 'D': 0}
        queue = deque(list(senate))
        while cnt['R'] != 0 and cnt['D'] != 0:
            c = queue.popleft()
            if c == 'R':
                if curr_cnt['R'] < 0:
                    curr_cnt['R'] += 1
                    cnt['R'] -= 1
                else:
                    curr_cnt['D'] -= 1
                    queue.append(c)
            else:
                if curr_cnt['D'] < 0:
                    curr_cnt['D'] += 1
                    cnt['D'] -= 1
                else:
                    curr_cnt['R'] -= 1
                    queue.append(c)
        return "Radiant" if cnt['D'] == 0 else "Dire" 