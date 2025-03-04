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