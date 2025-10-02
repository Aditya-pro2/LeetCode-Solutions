class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        m, ch = releaseTimes[0], keysPressed[0]
        for i in range(1, len(releaseTimes)):
            x = releaseTimes[i] - releaseTimes[i - 1]
            if m < x:
                m, ch = x, keysPressed[i]
            elif m == x and ch < keysPressed[i]:
                ch = keysPressed[i]
        return ch