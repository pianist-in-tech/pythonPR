#cannot be hashed
#Lists are mutable, meaning their content can change, which would change their hash value

#list
nums = [10, 20, 30, 40, 50]

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

#removing
nums.remove(30) #removes first accurance
popped = nums.pop() #removes last element

#sorting
nums.sort() #ascending
nums.sort(reverse=True) #Decending

#list comprehension
#new_list = [expression for item in iterable if condition]
squared = [x**2 for x in nums if x != 50] 
print(nums) 
print(popped) 
print(squared) 