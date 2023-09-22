class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = "abcdefghijklmnopqrstuvwxyz"
        l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        x = []
        for i in words:
            t = ""
            for j in range(len(i)):
                t += l[s.index(i[j])]
            x.append(t)
        return len(set(x))