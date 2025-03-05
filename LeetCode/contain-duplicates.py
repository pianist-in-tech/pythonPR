'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
'''

def containsNearbyDuplicate(nums, k):
#define an empty dictionary
    uniqueInts = {}
#iterate through the list using two point method (i and i-1 (considering that we start from the 1st index)
    for i in range(len(nums)):
#check for the duplicates: if the element is already in the dictionary, compare the current index with the index stored in the dictionary.
        if nums[i] in uniqueInts:
                #if yes, check the absolute condition
                if abs(i-uniqueInts[nums[i]]) <= k:               
                    return True          
#if no add the pair to the dictionary and keep iteration
        uniqueInts[nums[i]] = i 
#return false
    return False 