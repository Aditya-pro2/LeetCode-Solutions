class Solution:
    def findWords(self, w: List[str]) -> List[str]:
        l, s1, s2, s3 = [], "qwertyuiop", "asdfghjkl", "zxcvbnm"
        for i in w:
            p, a = i[0].lower(), 1
            x = s1 if p in s1 else s2 if p in s2 else s3
            for j in i[1:]:
                if j.lower() in x:
                    a += 1
            if a == len(i):
                l.append(i)
        return l