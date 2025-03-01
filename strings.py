#immutable

#slising (string[start:end(not included):step])

s = "PythonProgramming"

print(s[0:6])
print(s[:6])
print(s[6:])
print(s[-3:])
print(s[::-1]) #reverse
print(s[0:10:2])

#old-style formatting (%)
name = "Alice"
age = 25
print("my name is %s and I am %d years old." %(name, age)) 
#%s → Stands for string and is used to insert a string value. %d → Stands for integer and is used to insert an integer value.

#format() Method (more verbose)

print("my name is {} and I am {} years old.".format(name, age))
print("my name is {1} and I am {0} years old.".format(name, age)) #reordering
print("my name is {name} and I am {age} years old.".format(name='Alice', age=25)) #named placeholders

#f-strings (faster and more readable)

print(f'my name is {name} and I am{age} years old') 
print(f"next year, I will be {age + 1} years old.") 

#Regex Functions

import re

#re.match(pattern, string) - checks if the pattern appears AT THE BEGINNING of the string
result = re.match(r"Hello", "Hello, world!")
print(result)
print(bool(result))

#re.search(pattern, string) - finds the FIRST occurence of a pattern ANYWHERE in the string
result = re.search(r'world', 'hello, world')
print(result)
print(bool(result))

#re.findall(pattern, string) - returns ALL occurences of a pattern in a list
result = re.findall(r"\d+", "There are 43 apples and 5 oranges") #\d+ matches one or more digits in a row
print(result)

#re.sub(pattern, replacement, string) - replaces occurences of a pattern
result = re.sub(r"\d+", "XX", "there are 42 apples and 7 oranges.")
print(result)

text = "contact me at john.doe@example.com or support@company.com"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)