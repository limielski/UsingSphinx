.. _functions0-0-video:

Defining Main Functions in Python - video
=========================================

Rich Bibby

https://realpython.com/courses/python-main-function/

Many programming languages have a special function that is automatically executed when an operating system starts to run a program. This function is usually called main() and must have a specific return type and arguments according to the language standard. On the other hand, the Python interpreter executes scripts starting at the top of the file, and there is no specific function that Python automatically executes.

Nevertheless, having a defined starting point for the execution of a program is useful for understanding how a program works. Python programmers have come up with several conventions to define this starting point.

By the end of this course, you’ll understand:

* What the special __name__ variable is and how Python defines it
* Why you would want to use a main() in Python
* What conventions there are for defining main() in Python
* What the best practices are for what code to put into your main()