class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        c = 0
        l = []
        for i in pick:
            if i[0] not in l and pick.count(i) > i[0]:
                c += 1
                l.append(i[0])
        return c