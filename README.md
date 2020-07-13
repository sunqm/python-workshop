# python-workshop
Python summer workshop


# Prerequisites
Students are expected to go through the following chapters of the official Python documentation (https://docs.python.org/3.7/tutorial/). This should not take too long to read but can give students a quick view of the Python basics. Students do not necessarily need to set up a Python environment for this (we'll teach how to do that later). They can leverage online Python interpreters to paste-and-run the example code, such as LeetCode (https://leetcode.com/playground/new/empty).
* Chapter 3
* Chapter 4 (4.1 - 4.7.3)
* Chapter 5 (5.1 - 5.6)
* Chapter 9 (9.3 - 9.5)

# Content
The course will give students an introduction to the programming language Python and some important libraries widely used in the financial industry. It will start with topics including Python environment setup, package management softwares, and core language features. It then will provide some in-depth tutorials to help students learn how to manipulate data with Numpy and Pandas, and visualize data with libraries such as Matplotlib. An real-world example will be used to illustrate how these tools can be used together in cleaning data. It will also cover advanced topics such as performance profiling/optimization, garbage collection/reference counting, JIT compiler, etc. After this course, we expect students to get comfortable with coding in Python for both general purpose and for exploratory data analysis. Students will be more prepared for later courses during the MFE program such as machine learning. We will be using Python 3.7 throughout this course although more recent versions have been released.


## Session 1
* Introduction to Python. History and current status. Comparison against other languages.
* Virtualbox. Installation and Python environment setup (homework). Introduction to Jupyter notebook.
* Install packages.  
* Built-in data types. Sequences, dictionaries and sets. 
* Functions. Arguments. Anonymous functions. Annotations.
* Closure and decorator. Scope rules. 

## Session 2
* Class. Static/class data and methods. Inheritance. Abstract base classes. 
* Context manager. 
* Project structure. Using IDE.
* Import mechanism.
* Quality assurance with unit testing. PEP8. Pylint. 

## Session 3
* Introduction to Numpy. What is vectorization, compared to the regular python loop. Vector-oriented programming
* Ufunc
* Numpy fancy index.
* (Optional) Numpy dtypes.
* (Optional) Numpy data serialization
* Brief introduction to Scipy. scipy.linalg
* Cython and numba and JIT compiler

## Session 4
* History and relationship with numpy
* Introduction to Pandas. 
* Multilevel index, pivot table, groupby. 　
* Dates and Times in Python.
* Data visualization with Matplotlib and others.
* Data cleaning & exploratory data analysis with a real-world example. 

## Session 5
* Introduction to standard libraries: itertools, functools, collections, etc. What kind you do with python’s standard library.
* OS library. Scripting with Python. Launching external commands with subprocess. Working with filesystems. 
* Multithreading/multiprocessing. Python GIL
* File I/O. Serialization (pickle, json, etc.) (possibly move to numpy session)

## Session 6
* Performance profiling and optimization (lprof in jupyter)
* Debugging tools (pdb in jupyter)
* Python object lifecycle, gc, reference counting (sys/inspect) and circular reference. 
  * - in arguments
  * - in closure and context manager
  * - in `__del__`
* Concept of Concurrency & parallelism./Coroutines/ yield


# Prerequisite
## Install VirtualBox
* Students using Windows operating systems are strongly recommended to install VirtualBox in order to use a unix-like environment. 
* Students using MacOS can optionally use VirtualBox. But it's also fine to use the native OSX environment.
* [Instructions to set up Ubuntu with VirtualBox](docs/virtualbox.md) 

## Install Miniconda
* [Instructions to install and setup conda](docs/conda.md)

## Install Jupyter Notebook
* [Instructions to install Jupyter notebook](docs/jupyter.md)

## Set up Github and learn git
* Create a Github account.
* Create a Github repository with name "baruch-mfe-python-summer". 
Follow the instructions [here](https://docs.github.com/en/github/getting-started-with-github/create-a-repo) to create a repository.
* Learn to use basic git command. Try to clone the repo to your computer and push some changes to remote. 
Here is a good tutorial: https://medium.com/@seancoyne/learn-git-in-15-minutes-17cecc142652
