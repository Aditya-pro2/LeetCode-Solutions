class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        x = min(money // 7, children)
        money -= 7 * x
        r = children - x
        if r == 1 and money == 3:
            x -= 1
        elif r == 0 and money > 0:
            x -= 1
        return x