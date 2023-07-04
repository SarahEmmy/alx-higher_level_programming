# Python - Everything is an Object

This project explores the concept that everything in Python is an object. It covers various aspects related to objects, classes, mutability, and immutability. The following topics are covered:

## Learning Objectives

- Understanding why Python programming is awesome
- Understanding what an object is
- Differentiating between a class and an object or instance
- Understanding the difference between immutable and mutable objects
- Understanding references and assignments
- Exploring aliases and how to identify identical variables
- Identifying if two variables are linked to the same object
- Displaying variable identifiers (memory addresses)
- Understanding mutability and immutability
- Exploring built-in mutable types
- Exploring built-in immutable types
- Understanding how Python passes variables to functions

## Resources

To better grasp the concepts covered in this project, it is recommended to consult the following resources:

- [9.10. Objects and values](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
- [9.11. Aliasing](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
- [Immutable vs mutable types](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747)
- [Mutation](https://www.programiz.com/python-programming/immutable-mutable-python)
- [9.12. Cloning lists](https://www.geeksforgeeks.org/cloning-list-python/)
- [Python tuples: immutable but potentially changing](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747)

## Enjoy Python Programming!

Python's object-oriented nature, combined with its simplicity and versatility, makes it an awesome language for a wide range of applications. By understanding the concepts of objects, classes, mutability, and immutability, you will have a solid foundation for building powerful and efficient programs. Dive into the exercises, explore the code snippets, and have fun discovering the magic of Python!

 Who am I?
What function would you use to print the type of an object?
1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?
2. Right count
In the following code, do a and b point to the same object? Answer with Yes or No.
3. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.
4. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.
5. Right count =+
In the following code, do a and b point to the same object? Answer with Yes or No.
6. Is equal
What do these 3 lines print?
7. Is the same
What do these 3 lines print?
8. Is really equal
What do these 3 lines print?
9. Is really the same
What do these 3 lines print?
10. And with a list, is it equal
What do these 3 lines print?
11. And with a list, is it the same
What do these 3 lines print?
12. And with a list, is it really equal
What do these 3 lines print?
13. And with a list, is it really the same
What do these 3 lines print?
14. List append
What does this script print?
15. List add
What does this script print?
16. Integer incrementation
What does this script print?
17. List incrementation
What does this script print?
18. List assignation
What does this script print?
19. Copy a list object
Write a function def copy_list(l): that returns a copy of a list.
20. Tuple or not?
a = ()
21. Tuple or not?
a = (1, 2)
22. Tuple or not?
a = (1)
23. Tuple or not?
a = (1, )
24. Who I am?
What does this script print?
25. Tuple or not
What does this script print?
26. Empty is not empty
What does this script print?
27. Still the same?
id(a) 139926795932424

a [1, 2, 3, 4] a = a + [5] id(a)

28. Same or not?
a [1, 2, 3]

id (a) 139926795932424 a += [4] id(a)

29. Python3: Mutable, Immutable... everything is object!
Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):
30. #pythonic
Write a function magic_string() that returns a string “Holberton” n times the number of the iteration (see code):
31. Low memory cost
Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.
32. int 1/3
julien@ubuntu:/python3$ cat int.py a = 1 b = 1 julien@ubuntu:/python3$
33. int 2/3
julien@ubuntu:/python3$ cat int.py a = 1024 b = 1024 del a del b c = 1024 julien@ubuntu:/python3$
34. int 3/3
julien@twix:/tmp/so$ cat int.py print("I") print("Love") print("Python") julien@ubuntu:/tmp/so$

## Usage

This project consists of various exercises and questions that delve into the concepts mentioned above. It also includes code snippets to demonstrate the behavior of objects and variables in different scenarios. The questions are organized into different sections:

- Section 0: Who am I? - Introduction to object types and type identification.
- Sections 1-13: Exploring references, assignments, aliases, and variable comparisons.
- Sections 14-17: Understanding list and integer operations.
- Sections 18-20: Working with lists, tuples, and their assignation and copying.
- Sections 21-27: Further exploration of tuples, empty objects, and memory addresses.
- Section 28: Comparing list operations and memory addresses.
- Sections 29-34: Additional exercises and challenges related to objects and memory management.

For any additional guidance or support, feel free to refer to the resources provided or seek assistance from the Python community. Happy coding!
