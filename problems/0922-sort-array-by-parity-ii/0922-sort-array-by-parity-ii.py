class Solution:
    def sortArrayByParityII(self, a):
        i, j, sz = 0, 1, len(a)
        while i < sz and j < sz:
            if a[i] % 2 == 0:
                i += 2
            elif a[j] % 2 == 1:
                j += 2
            else:
                a[i], a[j] = a[j], a[i]
                i += 2
                j += 2
        return a