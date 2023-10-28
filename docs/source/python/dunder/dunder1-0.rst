When Should You Use .__repr__() vs .__str__() in Python?
========================================================

by Stephen Gruppetta  Mar 22, 2023

https://realpython.com/python-repr-vs-str/

Table of Contents

* In Short: Use .__repr__() for Programmers vs .__str__() for Users
* How Can You Access an Object’s String Representations?
* Should You Define .__repr__() and .__str__() in a Custom Class?
* Conclusion

One of the most common tasks that a computer program performs is to display data. The program often displays this information to the program’s user. However, a program also needs to show information to the programmer developing and maintaining it. The information a programmer needs about an object differs from how the program should display the same object for the user, and that’s where .__repr__() vs .__str__() comes in.

A Python object has several special methods that provide specific behavior. There are two similar special methods that describe the object using a string representation. These methods are .__repr__() and .__str__(). The .__repr__() method returns a detailed description for a programmer who needs to maintain and debug the code. The .__str__() method returns a simpler description with information for the user of the program.

The .__repr__() and .__str__() methods are two of the special methods that you can define for any class. They allow you to control how a program displays an object in several common forms of output, such as what you get from the print() function, formatted strings, and interactive environments.

In this tutorial, you’ll learn how to differentiate .__repr__() vs .__str__() and how to use these special methods in the classes you define. Defining these methods effectively makes the classes that you write more readable and easier to debug and maintain. So, when should you choose Python’s .__repr__() vs .__str__?
