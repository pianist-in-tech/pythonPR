'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

#Solution 1 (O(n^2))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through each element in nums
        for i in range(len(nums)):
            # Check each subsequent element in nums
            for j in range(i + 1, len(nums)):
                # If the sum of the two numbers equals the target, return their indices
                if nums[i] + nums[j] == target:
                    return [i, j]
                
#Solution 2 (0(n))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  # Create an empty dictionary to store the value and index of each number

        for i, num in enumerate(nums):  # Loop through the list with the index (i) and value (num)
            complement = target - num  # Calculate the complement (what would complete the target sum)

            if complement in num_dict:  # Check if the complement exists in the dictionary
                return [num_dict[complement], i]  # If it exists, return the indices

            num_dict[num] = i  # Otherwise, store the number and its index in the dictionary