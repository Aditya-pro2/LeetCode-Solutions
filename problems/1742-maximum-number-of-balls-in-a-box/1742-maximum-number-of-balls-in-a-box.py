class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans = 0
        boxes = collections.defaultdict(int)
        for num in range(lowLimit, highLimit+1):
            box = 0
            while num:
                digit = num%10
                num = num//10
                box += digit
            boxes[box] +=1
            ans = max(ans, boxes[box])
        return ans