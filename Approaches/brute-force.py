'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

#Brute Force Approach
#To check all pairs in nums to see if they sum to the target
#Time Complexity: O(n^2) because for each element, you are checking all subsequent elements.
nums = [2,7,11,15]
target = 9

#excercise
len(nums)  # Returns 4
for i in range(len(nums)):  # This will loop through the indices: 0, 1, 2, 3
    print(i)

#solution
for i in range(len(nums)):  # Loops through the indices: 0, 1, 2, 3
    for j in range(i + 1, len(nums)):  # Loops through indices greater than i: 1, 2, 3 (when i = 0), 2, 3 (when i = 1), etc.
        if nums[i] + nums[j] == target:  # Check if nums[i] + nums[j] equals the target (9)
            print[i, j]