class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        l = sentence.split()
        for i in range(len(l)):
            if l[i][0].lower() not in "aeiou":
                l[i] = l[i][1:] + l[i][0]
            l[i] += ("ma" + ("a" * (i + 1)))
        return " ".join(l)