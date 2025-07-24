class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        def dfs(u):
            nonlocal time
            time += 1
            timeIn[u] = time
            acc = nums[u]
            for w in adj[u]:
                if w == parents[u]:
                    continue
                parents[w] = u
                acc ^= dfs(w)
            subXOR[u] = acc
            timeOut[u] = time
            return acc
        
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parents, childs = [-1]*n, []
        timeIn, timeOut = [0]*n, [0]*n
        subXOR = [0]*n
        time = 0

        parents[0] = 0
        dfs(0)

        for u,v in edges:
            if parents[v] == u:
                childs.append((v,u))
            else:
                childs.append((u,v))
        m = len(childs)
        score = float('inf')
        
        for i in range(m):
            child1, end1 = childs[i]
            a1 = subXOR[child1]
            for j in range(i+1, m):
                child2, point2 = childs[j]
                a2 = subXOR[child2]
                if timeIn[child1] <= timeIn[child2] <= timeOut[child1]:
                    x1, x2, x3 = a2, a1 ^ a2, subXOR[0] ^ a1
                elif timeIn[child2] <= timeIn[child1] <= timeOut[child2]:
                    x1, x2, x3 = a1, a2 ^ a1, subXOR[0] ^ a2
                else:
                    x1, x2, x3 = a1, a2, subXOR[0] ^ a1 ^ a2
                score = min(score, max(x1, x2, x3) - min(x1, x2, x3))

        return score