How to Use Type Hints for Multiple Return Types in Python
=========================================================

by Claudia Ng

`źródło: <https://realpython.com/python-type-hints-multiple-types/?utm_source=notification_summary&utm_medium=email&utm_campaign=2023-10-20>`_

Table of Contents

* Use Python’s Type Hints for One Piece of Data of Alternative Types
* Use Python’s Type Hints for Multiple Pieces of Data of Different Types
* Declare a Function to Take a Callback
* Annotate the Return Value of a Factory Function
* Annotate the Values Yielded by a Generator
* Improve Readability With Type Aliases
* Leverage Tools for Static Type Checking
* Conclusion

In Python, type hinting is an optional yet useful feature to make your code easier to read, reason about, and debug. With type hints, you let other developers know the expected data types for variables, function arguments, and return values. As you write code for applications that require greater flexibility, you may need to specify multiple return types to make your code more robust and adaptable to different situations.

You’ll encounter different use cases where you may want to annotate multiple return types within a single function in Python. In other words, the data returned can vary in type. In this tutorial, you’ll walk through examples of how to specify multiple return types for a function that parses a string from an email address to grab the domain name.

In addition, you’ll see examples of how to specify type hints for callback functions or functions that take another function as input. With these examples, you’ll be ready to express type hints in functional programming.

.. note::
   Typically, you want to work with functions that are generous in which type of arguments they accept, while they’re specific about the type of their return value. For example, a function may accept any iterable like a list, tuple, or generator, but always return a list.
   If your function can return several different types, then you should first consider whether you can :ref:`refactor <refactoring0-1>` it to have a single return type. In this tutorial, you’ll learn how to deal with those functions that need multiple return types.