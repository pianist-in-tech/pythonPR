#cannot be hashed
#Lists - ordered, mutable collection, can hold mixed data types

#list
nums = [10, 20, 30, 40, 50, 20]
mixed = [1, 'hello', 3.14, True]

#indexing
print(nums[0])
print(nums[-1])

#slicing
#sequence[start:stop(exclusive):step(optional)]
print(nums[1:4])
print(nums[::-1]) #reverse
print(nums[:4]) #default start is 0
print(nums[1:]) #from 1 to end
print(nums[:]) #full copy
print(nums[-4:-1]) #from the end

#adding
nums.append(60)
nums.insert(2, 25) #(index, what to insert)

#removing (modifies the list in place and returns None.)'''

# Why use it?
# If you only need to remove one occurrence of a value and don’t need a return value, .remove() is fine.
# If you want a new list, use list comprehension instead

nums.remove(30) #removes first accurance
popped = nums.pop() #removes last element

#sorting
nums.sort() #ascending
nums.sort(reverse=True) #Decending

#list comprehension
#new_list = [expression for item in iterable if condition]
squared = [x**2 for x in nums if x != 50] 
evens = [x for x in range(10) if x % 2 == 0]

print(nums) 
print(popped) 
print(squared) 


# List Comprehension
nums = [1, 2, 3, 4, 5]
squared = [x**2 for x in nums]
print(squared) 

#COMMON PITFALLS
#Lists can change, which can cause unexpected behavior

a = [1, 2, 3]
b = a
b.append(4)
print(a) #[1, 2, 3, 4] - modifying b also changes a

#Fix: 
b=a.copy()
b=a[:] #to create an independend copy

#quick check
#print(nums[100]) #IndexError: list index out of range

#remove all occurances of a value
def remove_all_occur(nums, val):
    return [x for x in nums if x != val]  # Creates a new list without `val`

nums = [10, 20, 30, 20, 40, 20, 50]
nums = remove_all_occur(nums, 20)  
print(nums)  # [10, 30, 40, 50]


nums = [1, 2, 3, 4, 5]
copy_nums = nums  # Not using slicing!
copy_nums[0] = 100
print(nums)  #nums is changed now

nums = [1, 2, 3, 4, 5]
copy_nums = nums[:]
copy_nums[0] = 100
print(nums) #nums won't change: [1, 2, 3, 4, 5]

nums = [[1, 2, 3], [4, 5, 6]]
copy_nums = nums[:] #the inner lists are still the same objects in memory (they are not copied)
copy_nums[0][0] = 100
print(nums)  #nums will change 

#solution for deep copy
import copy
copy_nums = copy.deepcopy(nums)  # ✅ Fully independent copy
copy_nums[0][0] = 100
print(nums)  #nums will NOT change 