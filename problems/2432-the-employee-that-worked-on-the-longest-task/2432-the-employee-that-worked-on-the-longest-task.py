class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        m, idx = logs[0][1], logs[0][0]
        for i in range(1, len(logs)):
            x = logs[i][1] - logs[i - 1][1]
            if m < x:
                m, idx = x, logs[i][0]
            elif m == x and idx > logs[i][0]:
                idx = logs[i][0]
        return idx