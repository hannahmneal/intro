
#------------------------------------------------------------------------------------------------------------
# If this section is uncommented, the list, dictionary, set, and tuple examples below do not print.
#------------------------------------------------------------------------------------------------------------


# # 1. This is a "dictionary" in Pythonland.
# SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
#             1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# # 2. Instead of the word `function`, in Python, you use `def`
# def approximate_size(size, a_kilobyte_is_1024_bytes=True):

#     '''Convert a file size to human-readable form.
#     Keyword arguments:
#     size -- file size in bytes
#     a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
#                                 if False, use multiples of 1000
#     Returns: string
#     '''
#     if size < 0:
#         raise ValueError('number must be non-negative')

#     multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

#     # In Python, to use an "if" and "for" block, you use a colon and indent the corresponding code.
#     for suffix in SUFFIXES[multiple]:
#         size /= multiple
#         if size < multiple:
#             return '{0:.1f} {1}'.format(size, suffix)

#     raise ValueError('number too large')

# if __name__ == '__main__':
#     print(approximate_size(16384, False))
#     print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=True))
#     print(approximate_size(-16384))

#------------------------------------------------------------------------------------------------------------
# This is an example of a list in Python:
#------------------------------------------------------------------------------------------------------------

junk = list()
junk = ['carrots', 'celery', 'kale', 2, ['peas', 'corn']]
junk.insert(0, 'kidney beans')
# Note: if this were to read junk.insert(1, 'kidney beans'), kidney beans would be listed second in the array. Lists and their indices work the same was in Python as JS arrays.
# print(junk)
    # The result of a "print" at this point provides the following in the CLI: ['kidney beans', 'carrots', 'celery', 'kale', 2, ['peas', 'corn']]
junk.extend([True, 'tornado'])
#list.extend(iterable): Extends the list by appending all the items from the iterable.
# print(junk)
    # Result: ['kidney beans', 'carrots', 'celery', 'kale', 2, ['peas', 'corn'], True, 'tornado']
junk.append('hurricane')
# list.append: Adds an item to the end of a list.
print(junk)
# Result: ['kidney beans', 'carrots', 'celery', 'kale', 2, ['peas', 'corn'], True, 'tornado', 'hurricane']


# My own personal testing of list methods:

# otherCats = list()
# otherCats = ['Mira', 'Princess']

# cats = list()
# cats = ['Clove', 'Sage', 'Moses']
# cats.append('Lady')
# cats.extend(otherCats)
# cats.insert(2, 'Rosco')
# print(cats)


#------------------------------------------------------------------------------------------------------------
# Dictionary:
#------------------------------------------------------------------------------------------------------------


junk = dict()
junk = { 'name': 'Steve', 'age': 47, 'role': 'Head Coach' }
# print(junk)
    # The result at this point is ['kidney beans', 'carrots', 'celery', 'kale', 2, ['peas', 'corn'], True, 'tornado', 'hurricane']
    # from the list above and
    # {'name': 'Steve', 'age': 47, 'role': 'Head Coach'}
    # from the new dictionary here
junk['kids'] = 2
# Apparently, this creates a new key/value pair:  kids : 2
print(junk)
# Result: the junk list is printed first, then this: {'name': 'Steve', 'age': 47, 'role': 'Head Coach', 'kids': 2}

#------------------------------------------------------------------------------------------------------------
# Set: Each item in a Set must be unique. If you try to add two of the same item to a set, only one operation occurs.
#------------------------------------------------------------------------------------------------------------

junk = set()
junk.add('Scott')
junk.add('Scott')
print(junk)
# Result: { 'Scott' }

#------------------------------------------------------------------------------------------------------------
# Tuple: Iterating over the items in a tuple is faster than iterating over the items in a list. A tuple is immutable, however. This means items cannot be added or removed from it.
#------------------------------------------------------------------------------------------------------------

junk = tuple()
junk = ('Joe', 'Instructor', 'Awesome')
print(junk)

#------------------------------------------------------------------------------------------------------------


