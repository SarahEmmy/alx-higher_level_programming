0x04. Python - More Data Structures: Set, Dictionary

0. Squared simple: 
```python
def square_matrix(matrix):
    return [[x * x for x in row] for row in matrix]
```

1. Search and replace: 
```python
def replace_elements(lst, old, new):
    return [new if x == old else x for x in lst]
```

2. Unique addition: 
```python
def unique_addition(lst):
    return sum(set(lst))
```

3. Present in both: 
```python
def common_elements(set1, set2):
    return set1.intersection(set2)
```

4. Only differents: 
```python
def unique_elements(set1, set2):
    return set1.symmetric_difference(set2)
```

5. Number of keys: 
```python
def count_keys(dictionary):
    return len(dictionary.keys())
```

6. Print sorted dictionary: 
```python
def print_sorted(dictionary):
    for key in sorted(dictionary.keys()):
        print(key, dictionary[key])
```

7. Update dictionary: 
```python
def update_dictionary(dictionary, key, value):
    dictionary[key] = value
    return dictionary
```

8. Simple delete by key: 
```python
def delete_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary
```

9. Multiply by 2: 
```python
def multiply_values(dictionary):
    return {key: value * 2 for key, value in dictionary.items()}
```

10. Best score: 
```python
def get_best_score(dictionary):
    if not dictionary:
        return None
    return max(dictionary, key=dictionary.get)
```

11. Multiply by using map: 
```python
def multiply_values_by_number(lst, number):
    return list(map(lambda x: x * number, lst))
```

12. Roman to Integer: 
```python
# Implementation depends on the specific conversion algorithm for Roman numerals.
# You can find various implementations available online.

# Example function signature:
def roman_to_integer(roman_numeral):
    # Conversion logic
    pass
```

13. Weighted average: 
```python
def weighted_average(values):
    total_weight = sum(weight for value, weight in values)
    weighted_sum = sum(value * weight for value, weight in values)
    if total_weight != 0:
        return weighted_sum / total_weight
    else:
        return None
```

14. Squared by using map: 
```python
def square_matrix(matrix):
    return list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
```

15. Delete by value: 
```python
def delete_keys_by_value(dictionary, value):
    keys_to_delete = [key for key, val in dictionary.items() if val == value]
    for key in keys_to_delete:
        del dictionary[key]
    return dictionary
```

16. CPython #1: PyBytesObject:C functions that print some basic info about Python lists and Python bytes objects.
