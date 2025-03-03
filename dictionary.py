#allows fast lookups using hashing
#keys are unique and immutable
#values can be mutable

#dictionary
person = {
    'name':'Alice', 
    'age':25, 
    'city': 'NY'}

#accessing values
print(person['name'])
print(person.get('age')) #avoids KeyError

#adding & udating values
person['age'] = 26
person['job'] = 'engineer' # add new key-value pair

#removing elements
del person['city'] #removes that key
age = person.pop('age') #removes and returnes value

#iterating though
for key, value in person.items():
    print(f"{key}:{value}")

# print(person)

#collections.COUNTER
#great for counting occurences

from collections import Counter

#count frequency of characters in a string
text = "interview"
freq = Counter(text)
print(freq) 

#count words in a list
words = ["apple", "banana", "apple"]
word_count = Counter(words)
print(word_count)

#dictionary comprehension
#squaring numbers
squares = {x: x**2 for x in range(5)}
print(squares)

#checking key existence (in)
if "name" in person:
    print("Key exists")

# Di