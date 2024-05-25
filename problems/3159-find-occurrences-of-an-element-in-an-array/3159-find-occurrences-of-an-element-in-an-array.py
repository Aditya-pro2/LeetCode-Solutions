class Solution:
    def occurrencesOfElement(self, a: List[int], q: List[int], x: int) -> List[int]:
        d = [-1, ] * len(q)
        l = [-1, ]
        for i in range(len(a)):
            if a[i] == x:
                l.append(i)
        for i in range(len(q)):
            if q[i] < len(l):
                d[i] = l[q[i]]
        return d