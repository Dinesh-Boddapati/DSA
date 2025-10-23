# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        temp={} #temporary list to check the complement exists

        for i,num in enumerate(nums): 
            complement=target-num   # calc complement for each element of nums
            if complement in temp:   # to check if it exits 
                return temp(complement),i    #return indices
            temp[num]=i   #if it doesnt we push the element in num in to temp 
                          #Store the current number (num) as a key in the dictionary, and store its index (i) as the value.
        return None
