# intro

This is my project for studying and practicing exercises from the curriculum from NSS for Python/Django.

## Notes

To open the python interpreter, type `python` in the terminal (Mac OS). To close the interpreter, type `Ctrl+D`. For Windows, opening the interpreter is the same but closing it is done with `Ctrl+Z`. (1)

To execute a module of code from the CLI, type `python` then the name of the module (e.g., ` python humansizes.py` for this module). (1)



### Lists and Dictionaries

To create and print a list:
```
cats = list()
cats = ['Clove', 'Sage', 'Moses']
print(cats)
```

Other list methods can be found in the Python tutorial here: [The Python Tutorial - Documentation for version 3.6.8](https://docs.python.org/3.6/tutorial/datastructures.html). Here are three examples:

Given:

`myCats = ['Clove', 'Sage', 'Moses']`
`otherCats = ['Mira', 'Princess']`

`myCats.append('Lady')` : Adds 'Lady' to the end of the `cats` list. The result is: ['Clove', 'Sage', 'Moses', 'Lady']

`myCats.extend(otherCats)` : Extends the list by appending all the iterable items; in other words, it concatenates the first list (cats) with another iterable item (often but not exclusively another list). The result of this would be: ['Clove', 'Sage', 'Moses', 'Lady', 'Mira', 'Princess']

`myCats.insert(2, 'Rosco')` : Inserts a new item in the array at the position specified (2, in this case).


To create an print a dictionary:

```
cat = dict()
cat = {'name': 'Clove', 'age': 3, 'breed': 'calico shorthair'}
```

#### Exercises

[Python Stock Dictionary](https://github.com/nashville-software-school/bangazon-llc/blob/master/orientation/exercises/01_DICTIONARIES.md)








####




### Modules


## References

[Installations](https://github.com/nashville-software-school/bangazon-llc/blob/master/INSTALLATIONS.md)

#### 1.
[NSS Orientation - Importing Modules](https://github.com/nashville-software-school/bangazon-llc/blob/master/orientation/FND_02_IMPORTING.md)

#### 2.
[NSS Orientation - Types](https://github.com/nashville-software-school/bangazon-llc/blob/master/orientation/FND_03_TYPES.md)

#### 3.
[The Python Tutorial - Documentation for version 3.6.8](https://docs.python.org/3.6/tutorial/datastructures.html)


####
[Python - First Module](https://github.com/nashville-software-school/bangazon-llc/blob/master/orientation/FND_01_FIRST_MODULE.md)

