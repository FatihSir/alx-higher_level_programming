# **0x07. Python - Test-driven development**
![Test-driven development](1.jpeg)

This folder consists of python test-driven examples using [doctest](https://docs.python.org/3.4/library/doctest.html) and [unittest](https://docs.python.org/3.4/library/unittest.html).

### Before you start, make sure that you have knowledge about each item in the list below

    1- Why Python programming is awesome
    2- What’s an interactive test
    3- Why tests are important
    4- How to write Docstrings to create tests
    5- How to write documentation for each module and function
    6- What are the basic option flags to create tests
    7- How to find edge cases

## Usage
- Firstly, you should create a folder and name it ***Python_test***, which will contain the code to be tested
- Inside the ***Python_test*** folder, create another folder and name it ***tests***.
- The ***tests*** folder will contain the testing codes.


# Tasks
#### **0. Integers addition**

Write a function that adds 2 integers and name it **0-add_integer.py**.

- `Prototype: def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer or b must be an integer`
- `a` and `b` must be first casted to integers if they are float
- Returns an integer: the addition of `a` and `b`
- You are not allowed to import any module

#### **1. Divide a matrix**
Write a function that divides all elements of a matrix and name it **2-matrix_divided.py**.

- Prototype: `def matrix_divided(matrix, div):`
- matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message `matrix must be a matrix (list of lists) of integers/floats`
- Each row of the matrix must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
- div must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
- div can’t be equal to 0, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
- All elements of the matrix should be divided by `div`, rounded to 2 decimal places
- Returns a new matrix
- You are not allowed to import any module

#### **3. Print square**
Write a function that prints a square with the character `#`.

- Prototype: `def print_square(size):`
- size is the size length of the square
- size must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
- if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- if `size` is a float and is less than `0`, raise a `TypeError` exception with the message `size must be an integer`
- You are not allowed to import any module

#### **4. Text indentation**
Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`

- Prototype: `def text_indentation(text):`
- `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
- There should be no space at the beginning or at the end of each printed line
- You are not allowed to import any module
