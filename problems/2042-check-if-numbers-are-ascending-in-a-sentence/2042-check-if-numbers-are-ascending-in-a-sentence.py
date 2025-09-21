class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        count = float("-inf")
        s = s.split()
        for i in s:
            if i.isdigit():
                if int(i) > count:
                    count = int(i)
                else:
                    return False
        return True