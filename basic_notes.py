
"""
================ code flow in python =========== 

   user > python interpreter > machine languge > output .

=================== syntax ============== 

 Syntax is the set of rules used to write code in Python.

 ex. print ("hello")

============ semantics ==============

 Semantics refers to the meaning and logical interpretation of code

======== semantics error ============
"""

"""
================== Semantic Error (Logical Error) ====================

Definition:
A semantic error occurs when the syntax is correct, but the program logic is wrong.

Example:

length = 5
width = 10

area = length + width   # Wrong logic
print(area)

Correct:

area = length * width
print(area)

"""

"""

======== Case Sensitivity =======

Python is a case-sensitive language.

Example:

name = "Ali"
Name = "Ahmed"

print(name)
print(Name)

Output:

Ali
Ahmed

===== name and Name are different variables============

============== Indentation ===============

Definition:
Indentation is used to group statements together. Python uses indentation to define blocks of code.

Example:

if 10 > 5:
    print("True")

Without indentation:

if 10 > 5:
print("True")   # Error

"""

"""
 ============== Constants ============

Definition:
A constant is a value that should not change during program execution.

By convention, constants are written in UPPERCASE letters.

Example:

PI = 3.14
GRAVITY = 9.8

"""

"""
=============== Syntax Error ============

Definition:
A syntax error occurs when Python's grammar rules are violated.

Example:

if True
    print("Hello")

Output:

============== SyntaxError =============

Correct:

if True:
    print("Hello")
Name Error

Definition:
A NameError occurs when an undefined variable or identifier is used.

Example:

print(age)

Output:

NameError: name 'age' is not defined

Correct:

age = 20
print(age)

These are the complete notes from your notebook, typed neatly with proper formatting and examples.
"""