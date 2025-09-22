class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        n = len(arr2)
        ans = 0
        for num in arr1:
            idx = bisect_left(arr2, num)
            if idx == n:
                if abs(num - arr2[-1]) > d:
                    ans += 1
            elif idx == 0:
                if abs(num - arr2[0]) > d:
                    ans += 1
            elif abs(num - arr2[idx]) > d and abs(num - arr2[idx - 1]) > d:
                ans += 1
        return ans