'''
When Is It Used?
This method is usually used in problems where you need to look up whether a complement or previously seen value exists, as it provides an optimal time complexity of O(n).

It is ideal when:

You need to solve problems that involve finding pairs or complements (like in the two-sum problem).
You have a problem where you need to traverse a collection, store values, and look up those values efficiently.
Why This Works:
Hash maps (dictionaries) allow for constant-time lookups, meaning you can find if the complement of a number has been seen before in constant time (O(1)).
By storing already seen numbers along with their indices, you can immediately check if the complement of the current number exists, instead of checking all pairs like in the brute force approach.
Example Use Cases:
Finding pairs that sum to a target (like two-sum).
Finding duplicates in a list (i.e., first time you encounter a number, store it, and on encountering it again, you know it's a duplicate).
Checking if elements are in a collection before making decisions, optimizing for time complexity.
Example Problems:
Two Sum (where you need to find two numbers that add up to a given target).
Contains Duplicate (checking if a list has duplicate numbers).
Intersection of Two Arrays (finding common elements between two arrays).
In summary, this hash map approach is used when you're aiming to reduce the time complexity from O(n²) (brute force) to O(n). It’s an effective and common strategy for many algorithmic problems where efficient lookups and storing of elements are required.
'''
#two-sum problem
''' Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  # Create an empty dictionary to store the value and index of each number

        for i, num in enumerate(nums):  # Loop through the list with the index (i) and value (num)
            complement = target - num  # Calculate the complement (what would complete the target sum)

            if complement in num_dict:  # Check if the complement exists in the dictionary
                return [num_dict[complement], i]  # If it exists, return the indices

            num_dict[num] = i  # Otherwise, store the number and its index in the dictionary
