class ProductOfNumbers(object):
    l = []
    def __init__(self):
        self.l.append(1)

    def add(self, num: int) -> None:
        if num == 0:
            self.l = []
            self.l.append(1)
        else:
            self.l.append(self.l[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.l) - 1:
            return 0
        return self.l[-1] // self.l[-1 - k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)