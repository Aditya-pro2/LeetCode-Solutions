class Solution:
    def decodeMessage(self, k: str, m: str) -> str:
        l, x = [], []
        for i in range(len(k)):
            if k[i] != " " and k[i] not in k[:i]:
                l.append(k[i])        
        for i in range(len(m)):
            if m[i].isalpha():
                x.append(chr(l.index(m[i]) + 97))
            else:
                x.append(m[i])
        return "".join(x)