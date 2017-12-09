# Lists and tuples allow us to work with sequential data
# Sets unordered collection of values with no duplicates

# Lists have a lot more functionality

#Lists, values separated by a comma

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))
print(courses[0]) # access list item index 0
print(courses[-1]) # access list item on the last index (using -ve indexes)
print(courses[0:2]) # print range of values, first index inclusive, second not inclusive
print(courses[:2]) # assumes that we want to start from the begining
print(courses[2:]) # assumes that we want to go all the way to the end of the list

courses.append('Art') # adds Art to the end of the list

courses.insert(0,'Art') # add to specific index. Takes two arguments, the index and the value itself

# extend method when we have multiple values in our list

courses2 = ['Art', 'Education']
courses.insert(0, courses2) # creates a list within a list
courses.extend(courses2) # adds values from second list not the list itself

# Remove values from list
# use remove method

courses.remove('Math')

# Use pop method
courses.pop() # removes last item on the list
# It also returns value it removes

popped = courses.pop()

# Sort our list
# Reverse our list

courses.reverse() # last item becomes first

# Sort our list using sort method
courses.sort() # Sorts in alphabetic order or ascending order

# Reverse descending order
courses.sort(reverse=True)

sortedCourses = sorted(courses)
print(sortedCourses) # Sorted version of the list... not altering the original list

nums = [1,4,2,4]
print(min(nums)) # returns minimum value
print(sum(nums))

# Find the index of items in the list
print(couses.indes('CompSci'))

# Check if value is in the list
print('Art' in courses) # returns boolean - true false

for item in courses:
    print(item)

# Access the index using the enumerate function
for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start=1):
    print(index, course)


# turn our list to string using join method

course_str = ', '.join(courses)
print(course_str)

# turn string back to a list using split method
new_list = course_str.split(', ')


# tuples
# tuples are immutable (can't be changed)

# Mutable list
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2) # changing list 1 changes list 2 hence Mutable


# Imutable tuples
# use parenthesis instead of square brackets

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

tuple_1[0] = 'Art' # throws type error as tuple doesn't support item assignment
                    # immutable

print(tuple_1)
print(tuple_2)

# sets are values that are unordered and have no duplicates

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses) # prints out in any order
# sets throw away duplicates

print('Math' in cs_courses) # sets are special in this shit


cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Physics', 'CompSci'}

# use intersection method to see common ish

print(cs_courses.intersection(art_courses))

print(cs_courses.difference(art_courses)) # difference

print(cs_courses.union(art_courses)) # all courses printed out


# Summary
# creating empty lists, tuples and sets

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} # this is not right, creates a dictionary instead
empty_set = set()
