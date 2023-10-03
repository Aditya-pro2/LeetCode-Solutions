class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        x=0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0)+1
        freq=list(freq.items())
        for i in range(len(freq)):
            a=freq[i][1]
            if a>1:
                if a%2==0:
                    x+=(freq[i][1])
                else:
                    x+=(freq[i][1]-1)
                freq[i]=(freq[i][0],freq[i][1]%2)
        new=sorted(freq,key=lambda freq : (freq[1],freq[0]))
        return x+new[-1][1]