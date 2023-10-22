Python Scope & the LEGB Rule: Resolving Names in Your Code
==========================================================

by Leodanis Pozo Ramos  Mar 18, 2020
https://realpython.com/python-scope-legb-rule/

The concept of scope rules how variables and names are looked up in your code. It determines the visibility of a variable within the code. The scope of a name or variable depends on the place in your code where you create that variable. The Python scope concept is generally presented using a rule known as the LEGB rule.

The letters in the acronym LEGB stand for Local, Enclosing, Global, and Built-in scopes. This summarizes not only the Python scope levels but also the sequence of steps that Python follows when resolving names in a program.

* What scopes are and how they work in Python
* Why it’s important to know about Python scope
* What the LEGB rule is and how Python uses it to resolve names
* How to modify the standard behavior of Python scope using global and nonlocal
* What scope-related tools Python offers and how you can use them

.
.
.

.. scope0-0#globals:

globals()
---------

https://realpython.com/python-scope-legb-rule/#globals

In Python, globals() is a built-in function that returns a reference to the current global scope or namespace dictionary. This dictionary always stores the names of the current module. This means that if you call globals() in a given module, then you’ll get a dictionary containing all the names that you’ve defined in that module, right before the call to globals(). Here’s an example: