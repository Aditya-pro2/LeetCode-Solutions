class Solution:
    def convertTemperature(self, c: float) -> List[float]:
        return [round(c + 273.15, 5), round((c * 1.8) + 32, 5)]