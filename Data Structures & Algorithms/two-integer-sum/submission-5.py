class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for indice, value in enumerate(nums):
            remainder = target - value
            if remainder in dict1:
                return [dict1[remainder], indice]
            dict1[value] = indice