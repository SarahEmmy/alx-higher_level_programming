# Almost a Circle

This project focuses on implementing a set of classes and methods to handle rectangles and squares. The goal is to write code that is unit tested, follows PEP 8 style guidelines, and incorporates features such as serialization and deserialization.

## Learning Objectives

By completing this project, you should achieve the following learning objectives:

- Understand the concept of unit testing and its implementation in a large project.
- Learn how to serialize and deserialize a class.
- Gain knowledge on reading and writing JSON files.
- Familiarize yourself with *args and **kwargs and their usage.
- Handle named arguments in functions effectively.

## Resources

Before starting this project, it is recommended to review the following resources:

- args/kwargs
- JSON encoder and decoder
- unittest module
- Python test cheatsheet

## Requirements

1. Base class: Implement the class `Base`, which serves as the base for other classes.
2. First Rectangle: Create the class `Rectangle` that inherits from `Base`.
3. Validate attributes: Update the `Rectangle` class to include validation for setter methods and instantiation.
4. Area first: Add a public method `area(self)` to the `Rectangle` class that calculates and returns the area of the rectangle.
5. Display #0: Implement a public method `display(self)` in the `Rectangle` class that prints the rectangle using the character `#`.
6. str: Override the `__str__` method in the `Rectangle` class to provide a string representation of the rectangle.
7. Display #1: Improve the `display(self)` method in the `Rectangle` class to handle the rectangle's position (x, y).
8. Update #0: Extend the `Rectangle` class with a public method `update(self, *args)` that updates the rectangle's attributes.
9. Update #1: Modify the `update(self, *args)` method in the `Rectangle` class to also accept key/value arguments.
10. And now, the Square!: Implement the class `Square` that inherits from `Rectangle`.
11. Square size: Add getter and setter methods for the `size` attribute in the `Square` class.
12. Square update: Extend the `Square` class with a public method `update(self, *args, **kwargs)` that updates its attributes.
13. Rectangle instance to dictionary representation: Implement the `to_dictionary(self)` method in the `Rectangle` class, which returns a dictionary representation of the rectangle.
14. Square instance to dictionary representation: Add the `to_dictionary(self)` method to the `Square` class to return a dictionary representation of the square.
15. Dictionary to JSON string: Implement the class method `to_json_string(list_dictionaries)` in the `Base` class, which converts a list of dictionaries to a JSON string.
16. JSON string to file: Extend the `Base` class with the class method `save_to_file(cls, list_objs)` that saves the JSON string representation of a list of objects to a file.
17. JSON string to dictionary: Add the static method `from_json_string(json_string)` to the `Base` class, which converts a JSON string to a list of dictionaries.
18. Dictionary to Instance: Extend the `Base` class with the class method `create(cls, **dictionary)` that creates an instance with attributes set from a dictionary.
19. File to instances: Implement the class method `load_from_file(cls)` in the `Base` class, which loads and returns a list of instances from a file.
20. JSON ok, but CSV?: Extend the `Base` class with the class methods `save_to_file_csv(cls, list_objs)` and `load_from_file_csv(cls)`, which serialize and deserialize in CSV format.
21. Let's draw it: Add the static method `draw(list_rectangles, list_squares)` to the `Base` class, which opens a window and draws all the rectangles and squares provided.

## Testing and Validation

All files, classes, and methods should be unit tested, ensuring compliance with PEP 8 style guidelines.

Please refer to the provided resources for further information and guidance on completing this project.
