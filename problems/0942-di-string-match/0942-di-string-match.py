class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        a, b, x = 0, len(s), []
        for i in s:
            if i == "I":
                x.append(a)
                a += 1
            else:
                x.append(b)
                b -= 1
        return x + [b]