.. _dunder0-0-video:

What Does if __name__ == "__main__" Mean in Python?
===================================================

https://realpython.com/courses/if-name-main-python/

You’ve likely encountered Python’s if __name__ == "__main__" idiom when reading other people’s code. You might have even used if __name__ == "__main__" in your own scripts. But did you use it correctly?

This line of code can seem a little cryptic, so don’t fret if you’re not completely sure what it does, why you might want it, and when to use it.

In this video course, you’ll learn all about Python’s if __name__ == "__main__" idiom.


What Does if __name__ == "__main__" Mean in Python? (Summary)
Arianne Dee
What Does if __name__ == "__main__" Mean in Python?
Arianne Dee  03:36


Contents
Transcript
Discussion (5)
You’ve learned what the if __name__ == "__main__" idiom does in Python. It allows you to write code that executes when you run the file as a script, but not when you import it as a module. It’s best to use it when you want to collect user input during a script run and avoid side effects when importing your module—for example, to unit test its functions.

You also got to know some common but suboptimal use cases and learned about better and more idiomatic approaches that you can take in those scenarios. Maybe you’ve accepted Python’s name-main idiom after learning more about it, but if you still dislike it, then it’s good to know that you can probably replace its use in most cases.

For further investigation, check out:

📰 How to Run Your Python Scripts
🎬 Running Python Scripts
📰 Python Modules and Packages – An Introduction
🎬 Python Modules and Packages: An Introduction
📰 Defining Main Functions in Python
🎬 Defining Main Functions in Python
You can visit the following resources to lean more about testing in Python:

📰 Getting Started With Testing in Python
🎬 Test-Driven Development With pytest
These resources will help you document your projects with Python:

📰 Documenting Python Code: A Complete Guide
🎬 Documenting Python Code: A Complete Guide
📰 Python’s doctest: Document and Test Your Code at Once
Maybe you’d like to learn more about using the command line. Real Python’s got you covered:

📰 Python Command-Line Arguments
🎬 Command Line Interfaces in Python
📰 Build Command-Line Interfaces With Python’s argparse
🎬 Building Command Line Interfaces With argparse
When do you use the name-main idiom in your Python code? While working your way through this course, did you discover a way to replace it, or is there a good use case that we missed? Share your thoughts in the comments below.

