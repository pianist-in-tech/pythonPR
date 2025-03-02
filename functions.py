def add_numbers(a,b):
    #returns the sum of two numbers
    return a+b

result = add_numbers(3, 5)
print(result)

#lambda functions(anonymous) - small single-expression function without a name
#lambda arguments: expression

add = lambda x, y: x+y
print(add(3, 5))

numbers = [1, 2, 3, 4] #list
squared = list(map(lambda x:x**2, numbers))
print(squared)

'''
lambda x: x**2 → Lambda function

This is an anonymous function (a function without a name).
It takes one argument (x) and returns x**2 (which is x squared).
Example:
If x = 2, it returns 2**2 = 4.
If x = 3, it returns 3**2 = 9.
map(lambda x: x**2, numbers) → Applying lambda to every element

map(function, iterable) applies the function to each item in the iterable (numbers).
It does not return a list directly—it returns a map object (an iterator).
Example execution:
map(lambda x: x**2, [1, 2, 3, 4])
Computes:
1**2 → 1
2**2 → 4
3**2 → 9
4**2 → 16
Result: [1, 4, 9, 16] (but as a map object).
list(...) → Converting the result into a list

map() returns an iterator, so we convert it into a list using list(...).
Now, squared = [1, 4, 9, 16].
'''
