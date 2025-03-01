#unordered  collection of unique elements
#no duplicates allowed
#fast lookups, mutable but only stores immutable elements
#use hashing to store elements

#set
numbers = {1, 2, 3, 4, 5}
print(3 in numbers)

#adding & removing elements
numbers.add(6)
numbers.remove(2)
numbers.discard(10) #does nothing if element not found
print(numbers)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#union
print(A | B) #doesn't repeat repetitive elements

#intersection
print(A&B) #prints only those that were the same in both sets

#difference
print(A-B) #only considers elements in the first set that are not in the second set

math_students = {"Alice", "Bob", "Charlie", "David"}
science_students = {"Charlie", "David", "Eve", "Frank"}

only_math = math_students - science_students
print(only_math)  # Output: {'Alice', 'Bob'} (Students only in math)

#symmetric difference
print(A ^ B) #prints what's different in both sets

#hashing is used for fast lookups

print(hash("apple"))
print(hash(42))
print(hash((1, 2, 3)))

my_set = {"apple", "banana", "cherry"}
print("apple" in my_set)

#Not all objects can be added to a set. Mutable objects (e.g., lists, dictionaries) are unhashable because their content can change.