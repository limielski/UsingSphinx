Working With Python Virtual Environments
========================================

https://realpython.com/courses/working-python-virtual-environments/

Dan Bader 6 Lessons  8m

When you install Python packages globally there can be only one version of a Python library across all of your programs. This means you’ll quickly run into version conflicts.

The solution to these problems is separating your Python environments with so-called virtual environments. They allow you to separate Python dependencies by project, including selecting between different versions of the Python interpreter.

A Virtual Environment (or “virtualenv”, “venv” for short) is an isolated Python environment. Physically, it lives inside a folder containing all the packages and other dependencies, like native-code libraries and the interpreter runtime, that a Python project needs.

To demonstrate how virtual environments work as a “sandbox” I’ll give you a quick walkthrough where we’ll set up a new environment (or virtualenv, as they’re called for short) and then install a third-party package into it using the Python pip command.
