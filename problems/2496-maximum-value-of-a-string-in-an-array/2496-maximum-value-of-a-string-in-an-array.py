class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        m = 0
        for i in strs:
            if i.isdigit():
                m = max(m, int(i))
            else:
                m = max(m, len(i))
        return m