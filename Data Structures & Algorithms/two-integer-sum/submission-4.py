from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []
        list1 = []
        for i in range(len(nums)):
            list1.append(target - nums[i])
        
        intersection = list(set(list1) & set(nums))

        if len(intersection)==3:
            intersection.remove(target/2)
        elif len(intersection)==1:
            intersection.append(intersection[0])
        
        for i in range(len(nums)):
            if nums[i] == intersection[0]:
                indexes.append(i)
            elif nums[i] == intersection[1]:
                indexes.append(i)
        
        return indexes