# Dictionaries - allow us to work with key value pairs
# associative array in other programming languages
 
# like a real Dictionary

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name']) # pass in the name key

# access a key that doesn't exist, throws a key error
# instead of throwing an error we can instead something else, like a default or something using the get method

print(student.get('phone')) # returns none instead of an error

print(student.get('phone', 'Not found')) # adding a default value instead of an error


# update values
student['name'] = 'Mike'
# update values using the update method
student.update({'name': 'Ocho', 'age': 23, 'phoneNumber': 233234})

# delete key
del student['age']
# delete key using pop method... also returns the value
age = student.pop('age')
print(age) # prints the popped age and value

# print out length of values
print(len(student)) # prints number of keys

# print keys
print(student.keys())
print(student.items()) # key and value pairs

# loop through print keys
for key in student:
    print(key)

# loop through, print keys and values
for key, value in student.items():
    print(key, value)
