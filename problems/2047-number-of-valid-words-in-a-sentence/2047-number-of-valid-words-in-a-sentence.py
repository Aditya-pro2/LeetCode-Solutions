class Solution:
    def countValidWords(self, sentence: str) -> int:
        cnt = 0
        for w in sentence.split():
            ok = True
            h = p = 0
            for i, c in enumerate(w):
                if c.isdigit():
                    ok = False
                    break
                if c == "-":
                    h += 1
                    if (h > 1 or i == 0 or i == len(w) - 1 or not w[i - 1].isalpha() or not w[i + 1].isalpha()):
                        ok = False
                        break
                if c in "!.,":
                    p += 1
                    if p > 1 or i != len(w) - 1:
                        ok = False
                        break
            if ok:
                cnt += 1
        return cnt