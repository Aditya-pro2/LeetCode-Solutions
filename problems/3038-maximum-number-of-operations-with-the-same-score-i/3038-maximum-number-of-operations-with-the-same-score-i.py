class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        q, x, s = deque(nums), 0, None
        while (len(q) >= 2):
            a = q.popleft()
            b = q.popleft()
            y = a + b
            if (s is not None and y != s):
                break
            x += 1
            s = y
        return x