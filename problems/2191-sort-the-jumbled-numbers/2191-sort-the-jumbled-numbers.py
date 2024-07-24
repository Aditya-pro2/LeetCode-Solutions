class Solution:
    def sortJumbled(self, m: List[int], a: List[int]) -> List[int]:
        l, d = [], {}
        for i in a:
            s = ""
            for j in str(i):
                s += str(m[int(j)])
            n = int(s)
            if n in d:
                d[n].append(i)
            else:
                d[n] = [i]
        for i in sorted(d):
            for j in d[i]:
                l.append(j)
        return l