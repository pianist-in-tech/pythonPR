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
popped = nums.pop() #removes last e