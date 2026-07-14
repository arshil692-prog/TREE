"""
========= keywords ========


Definition

A keyword is a reserved word in Python that has a predefined meaning.

Python uses keywords to understand your program.

======== Characteristics of Keywords ==============

✅ Reserved words.
✅ Have predefined meanings.
✅ Cannot be used as variable names.
✅ Case-sensitive (True is a keyword, true is not).

ex . if = 10 

SyntaxError (becase if is keyword)

============ all keywords ========== 

Keyword	                           Purpose
False	                       Boolean false value
None	                       Represents no value
True	                       Boolean true value
and	                           Logical AND
as	                           Gives an alias
assert	                       Debugging check
async	                       Asynchronous programming
await	                       Wait for async task
break	                       Exit a loop
class	                       Create a class
continue	                   Skip current loop iteration
def	                           Define a function
del	                           Delete an object/reference
elif	                       Else if
else	                       Alternative block
except	                       Handle exceptions
finally	                       Always execute this block
for	                           Create a loop
from	                       Import specific items
global	                       Access global variable
if	                           Conditional statement
import	                       Import a module
in	                           Membership test
is	                           Identity comparison
lambda	                       Anonymous function
nonlocal	                   Access enclosing scope variable
not	                           Logical NOT
or	                           Logical OR
pass	                       Placeholder statement
raise	                       Raise an exception
return	                       Return value from a function
try	                           Start exception handling
while	                       Create a while loop
with	                       Context manager
yield	                       Return values one at a time from a generator


=========== definations ==============
A keyword is a reserved word with a special meaning in Python.

Keywords cannot be used as identifiers (variable, function, or class names).

Modern Python has 35 keywords (this may change in future versions).

Use the keyword module to list keywords or check whether a word is a keyword.

Learning keywords is essential because they form the foundation of Python syntax and appear in almost every Python program.

================ intiviwe ===========

1. What is a keyword in Python?

A keyword is a reserved word with a predefined meaning that Python uses to understand the structure of a program.


2. Can we use keywords as variable names?

No. Doing so results in a SyntaxError.


3. How can you see all Python keywords?
import keyword

print(keyword.kwlist)


4. How do you check if a word is a keyword?
import keyword

print(keyword.iskeyword("for"))


5. Are keywords case-sensitive?

Yes.

True ✅ Keyword
true ❌ Not a keyword

"""