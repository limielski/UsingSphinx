Bypassing the GIL for Parallel Processing in Python
===================================================

https://realpython.com/python-parallel-processing/

zmiana po przywróceniu

* Recall the Fundamentals of Parallel Processing
   * What’s Parallel Processing?
   * How Do CPU-Bound and I/O-Bound Tasks Differ?
   * Why Do Modern Computers Favor Parallelism?
   * How Can You Harness the Power of Multiple CPU Cores?
* Compare Multithreading in Python and Other Languages
   * Java Threads Solve CPU-Bound and I/O-Bound Problems
   * Python Threads Only Solve I/O-Bound Problems
   * Python’s GIL Prevents Threads From Running in Parallel
   * The GIL Ensures Thread Safety of the Python Internals
* Use Process-Based Parallelism Instead of Multithreading
   * multiprocessing: Low-Level Control Over Processes
   * concurrent.futures: High-Level Interface for Running Concurrent Tasks
* Make Python Threads Run in Parallel
   * Use an Alternative Runtime Environment for Python
   * Install a GIL-Immune Library Like NumPy
   * Write a C Extension Module With the GIL Released
   * Have Cython Generate a C Extension Module for You
   * Call a Foreign C Function Using ctypes
* Try It Out: Parallel Image Processing in Python
   * Make a Graphical User Interface Using Tkinter
   * Define a Command-Line Interface With argparse
   * Display a Scaled-Down Preview of the Loaded Image
   * Interact With Your Application Through Mouse Events
   * Write a C Function to Calculate the Pixel Formula
   * Process Color Channels in Separate Threads of Execution
   * Build a Lookup Table for Common Pixel Values
   * Share Memory Between Python and C Through Pointers
* Conclusion

Unlocking Python’s true potential in terms of speed through shared-memory parallelism has traditionally been limited and challenging to achieve. That’s because the global interpreter lock (GIL) doesn’t allow for thread-based parallel processing in Python. Fortunately, there are several work-arounds for this notorious limitation, which you’re about to explore now!

