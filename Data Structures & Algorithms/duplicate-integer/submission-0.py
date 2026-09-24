class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # print(nums)
        seen = set()
        for num in nums:
            # print("Number is",num)
            if num in seen:
                # print(num,"already in Set:",seen)
                return True
            else:
                seen.add(num)
                # print(num,"added in Set:",seen)
        
        seen = None
        return False
            # situation 1 and situation 2 go here