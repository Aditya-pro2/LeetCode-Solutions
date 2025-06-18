class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        return (n:=sorted(nums)) and ([] if any(n[3*i+2]-n[3*i]>k for i in range(len(n)//3)) else [n[3*i:3*i+3] for i in range(len(n)//3)])