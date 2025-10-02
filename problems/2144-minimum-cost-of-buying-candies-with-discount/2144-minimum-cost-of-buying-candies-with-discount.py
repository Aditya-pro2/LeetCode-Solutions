class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        n = len(cost)
        i = s = 0
        while i < n:
            if i + 1 == n:
                s += cost[i]
                break
            s += (cost[i] + cost[i + 1])
            if i + 2 == n:
                break
            i += 3
        return s