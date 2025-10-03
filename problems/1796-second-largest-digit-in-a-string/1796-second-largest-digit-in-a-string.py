class Solution:
    def secondHighest(self, s: str) -> int:
        l = set()
        for i in s:
            if i.isdigit():
                l.add(int(i))
        if len(l) <= 1:
            return -1
        return sorted(l)[-2]