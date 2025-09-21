class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        l, c = 1, 0
        for i in s:
            x = widths[ord(i) - 97]
            if c + x > 100:
                c = x
                l += 1
            else:
                c += x
        return [l, c]