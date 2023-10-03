class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
        ans = ''
        c = 0
        while num1 or num2 or c:
            s = c
            if num1:
                s += dic[num1[-1]]
                num1 = num1[:-1]
            if num2:
                s += dic[num2[-1]]
                num2 = num2[:-1]
            c = s // 10
            ans = str(s %10) + ans
        return ans