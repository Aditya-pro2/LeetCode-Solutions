class Solution:
    def greatestLetter(self, s: str) -> str:        
        store = list(filter(lambda x: x.islower(), set(s)))
        storeup = list(filter(lambda x: x.isupper(), set(s)))
        letter = ''
        for i in storeup:
            if chr(ord(i) + 32) in store:
                if letter < i:
                    letter = i
        return letter