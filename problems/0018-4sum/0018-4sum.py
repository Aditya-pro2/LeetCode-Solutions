class Solution:
    def fourSum(self, a: List[int], target: int) -> List[List[int]]:
        n, x = len(a), []
        a.sort()
        for i in range(n - 3):
            if i > 0 and a[i] == a[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and a[j] == a[j - 1]:
                    continue
                l, h = j + 1, n - 1
                while l < h:
                    t = a[i]+ a[j] + a[l] + a[h]
                    if t == target:
                        x.append([a[i], a[j], a[l], a[h]])
                        while l < h and a[l] == a[l + 1]:
                            l += 1
                        l += 1
                        while l < h and a[h] == a[h - 1]:
                            h -= 1
                        h -= 1
                    elif t < target:
                        l += 1
                    else:
                        h -= 1
        return x