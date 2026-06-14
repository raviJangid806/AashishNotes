# Python Basics Notes

## 1. Introduction to Python
- Python is a high-level, interpreted programming language.
- Designed for readability and ease of use.
- Uses indentation instead of braces to define code blocks.
- Supports multiple programming paradigms: procedural, object-oriented, and functional.
- Python files use the `.py` extension.

## 2. Installing Python
- Download from https://www.python.org/downloads/
- Verify installation with `python --version` or `python3 --version`.
- Use `pip` to install packages: `pip install package-name`.
- On Windows, add Python to PATH during installation.

## 3. Running Python Code
- Run a script file: `python script.py`.
- Use the interactive shell by typing `python` or `python3`.
- Use code editors or IDEs like VS Code, PyCharm, or Jupyter Notebook.

## 4. Basic Python Syntax
### 4.1 Comments
- Single-line comment: `# This is a comment`
- Multi-line comment / docstring: `"""This is a multi-line comment"""`

### 4.2 Variables and Data Types
- Variables are created when first assigned.
- Common data types:
  - `int` for integers, e.g. `5`
  - `float` for decimals, e.g. `3.14`
  - `str` for strings, e.g. `'hello'` or `"hello"`
  - `bool` for boolean values: `True` or `False`
  - `list` for ordered collections: `[1, 2, 3]`
  - `tuple` for immutable collections: `(1, 2, 3)`
  - `dict` for key-value pairs: `{"name": "Alice", "age": 30}`
  - `set` for unique items: `{1, 2, 3}`

### 4.3 Variable Assignment
- Assign values with `=`: `x = 10`
- Multiple assignments:
  - `a, b = 1, 2`
  - `x = y = 0`

### 4.4 Printing Output
- Use `print()` to display values.
  - `print("Hello, world!")`
  - `print(x, y)`
  - `print(f"Value is {x}")` for f-strings.

### 4.5 Taking Input
- Use `input()` to read from the user.
  - `name = input("Enter your name: ")`
  - Convert types: `age = int(input("Enter age: "))`

## 5. Operators
### 5.1 Arithmetic Operators
- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `//` integer division
- `%` modulus remainder
- `**` exponentiation

### 5.2 Comparison Operators
- `==` equal
- `!=` not equal
- `>` greater than
- `<` less than
- `>=` greater than or equal
- `<=` less than or equal

### 5.3 Logical Operators
- `and` logical AND
- `or` logical OR
- `not` logical NOT

### 5.4 Assignment Operators
- `=` basic assignment
- `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` for shorthand updates

## 6. Control Flow
### 6.1 If Statements
- Syntax:
  ```python
  if condition:
      # code
  elif other_condition:
      # code
  else:
      # code
  ```
- Example:
  ```python
  x = 10
  if x > 0:
      print("Positive")
  elif x == 0:
      print("Zero")
  else:
      print("Negative")
  ```

### 6.2 While Loops
- Syntax:
  ```python
  while condition:
      # code
  ```
- Example:
  ```python
  i = 0
  while i < 5:
      print(i)
      i += 1
  ```

### 6.3 For Loops
- Syntax:
  ```python
  for item in iterable:
      # code
  ```
- Example:
  ```python
  for i in range(5):
      print(i)
  ```
- `range()` function details:
  - `range(5)` → 0,1,2,3,4
  - `range(1, 5)` → 1,2,3,4
  - `range(1, 10, 2)` → 1,3,5,7,9

### 6.4 Loop Control Statements
- `break` stops the loop.
- `continue` skips the current iteration.
- `pass` does nothing, used as a placeholder.

## 7. Data Structures
### 7.1 Lists
- Ordered, changeable collection.
- Create: `numbers = [1, 2, 3]`
- Access: `numbers[0]`, `numbers[-1]`
- Modify: `numbers[1] = 5`
- Methods:
  - `append()` add item
  - `insert()` add at index
  - `remove()` remove first matching value
  - `pop()` remove by index
  - `sort()` sort items
  - `reverse()` reverse items

### 7.2 Tuples
- Ordered, immutable collection.
- Create: `point = (1, 2)`
- Access: `point[0]`
- Use when values should not change.

### 7.3 Dictionaries
- Key-value pairs.
- Create: `person = {"name": "Alice", "age": 30}`
- Access: `person["name"]`
- Add/change: `person["city"] = "Paris"`
- Methods:
  - `keys()`, `values()`, `items()`
  - `get()` returns value or default if key missing
  - `pop()` removes key and returns value

### 7.4 Sets
- Unordered collection of unique items.
- Create: `colors = {"red", "green"}`
- Add: `colors.add("blue")`
- Remove: `colors.remove("red")`
- Useful for membership tests and deduplication.

## 8. Functions
- Define with `def`:
  ```python
  def greet(name):
      return f"Hello, {name}!"
  ```
- Call with `greet("Alice")`.
- Return values with `return`.
- Parameters:
  - required parameters
  - default parameters: `def greet(name="Guest"):`
  - keyword arguments: `greet(name="Bob")`
  - arbitrary arguments: `*args`, `**kwargs`
- Example with both:
  ```python
  def add_numbers(*nums):
      return sum(nums)
  ```

## 9. Modules and Packages
- A module is a `.py` file containing Python code.
- Import modules using `import module_name`.
- Example: `import math`, `from math import sqrt`
- Packages are directories with an `__init__.py` file.
- Use `pip install` for third-party packages.

## 10. File Handling
- Open a file with `open()`.
- Example:
  ```python
  with open("example.txt", "r") as file:
      content = file.read()
  ```
- Modes:
  - `r` read
  - `w` write (overwrite)
  - `a` append
  - `x` create new file
  - `b` binary mode
  - `t` text mode
- Always close files or use `with` for safe handling.

## 11. Error Handling
- Use `try`, `except`, `else`, `finally`.
- Example:
  ```python
  try:
      result = 10 / 0
  except ZeroDivisionError:
      print("Cannot divide by zero")
  else:
      print("Success")
  finally:
      print("Cleanup")
  ```

## 12. Basic Object-Oriented Programming
- Class definition:
  ```python
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      def greet(self):
          print(f"Hello, I am {self.name}")
  ```
- Create instance: `p = Person("Alice", 30)`
- Access attributes: `p.name`
- Call methods: `p.greet()`
- Inheritance:
  ```python
  class Student(Person):
      def __init__(self, name, age, grade):
          super().__init__(name, age)
          self.grade = grade
  ```

## 13. Useful Built-in Functions
- `len()` length of object
- `type()` type of an object
- `str()`, `int()`, `float()` type conversions
- `range()` iterate sequence of numbers
- `enumerate()` loop with index
- `zip()` combine iterables
- `min()`, `max()`, `sum()`
- `sorted()` sort iterable

## 14. Basic Formatting and Style
- Use 4 spaces per indentation level.
- Keep lines under 79 characters when possible.
- Use descriptive variable names.
- Add comments where needed.
- Follow PEP 8 style guidelines.

## 15. Example Python Program
```python
# Simple program to check even or odd numbers
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

## 16. Basic Python Formatting Examples
- String concatenation: `"Hello " + "World"`
- Formatted string literal: `f"Hello, {name}!"`
- Multi-line string:
  ```python
  message = """This is a
  multi-line string."""
  ```
- List comprehension:
  ```python
  squares = [x*x for x in range(5)]
  ```

## 17. Summary
- Python is beginner-friendly with simple syntax.
- Start with variables, conditionals, loops, and functions.
- Practice data structures like lists, dictionaries, and sets.
- Learn modules, file handling, and basic error handling next.
- Use an editor and run code often to build confidence.
