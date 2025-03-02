#enumerate is a built-in Python function that allows you to iterate through a list (or any iterable) while keeping track of the index of the current item. It returns each item as a tuple, where the first element is the index and the second is the value.
#enumerate(iterable, start=0)
# iterable: The list or any iterable you want to loop through.
# start: The starting index. By default, it's 0, but you can change it.

nums = [2, 7, 11, 15]
for i, num in enumerate(nums): #i,num will turn into returned tuple here
    print(i, num)
    
# output:
# 0 2
# 1 7
# 2 11
# 3 15
# Here, i is the index of the item, and num is the value of that item.

# 2. Using enumerate() outside the loop (e.g., converting it into a list):
# You can call enumerate(nums) and convert it into a list or another collection to see the index-value pairs all at once.

nums = [2, 7, 11, 15]
enumerated_list = list(enumerate(nums)) # "list()" internally loops over "enumerate(nums)"
print(enumerated_list)
#Output:
[(0, 2), (1, 7), (2, 11), (3, 15)]
# In this case, enumerate(nums) returns an iterator, which you can convert to a list (or any other iterable) if you want to view all the index-value pairs at once.

