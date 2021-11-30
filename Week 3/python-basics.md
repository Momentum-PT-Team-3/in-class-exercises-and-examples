# Python Basics

---
## Basic Data Types
_There are more than these, but these are the types we will handle the most._

- **Numbers**  
	- Integers (Positive and negative whole numbers, including 0) 
		- ```3, 9, 0, -5```   
	- Floats (Decimals BUT they are inexact and should not be used for money).  
		- ```5.9, -0.14, 4.0```

---

- **Strings**
	- Collections of characters. Can be letters, numbers, symbols, or spaces.
		```"Beyoncé", "Chapter 1", "!@#$%!"```  

- **Booleans**
	- Like an on/off switch or a lightbulb. Two options for values, either ```True``` or ```False```  
	- Beyond these two values, there are values that are considered "truthy or falsy" because they can be [represented with a Boolean](https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/).

- **None Type**
	In Python, when a value does not exist, we use the keyword ```None```. This is different from 0, which is an integer.
---

- Python has **built-in methods** to convert one type to another.
	- ```int()``` converts a string or float to an integer. Note it does NOT round floats. It eliminates everything to the right of the decimal point.
	- ```str()``` converts a number or float to a string
	- ```float()``` converts a string or integer to a float
	- ```bool()``` shows the Boolean representation of a value of another data type (truthy or falsy)
___

## Variables and Functions

- **Variables** are like containers that hold values in memory. More accurately, they are markers that point to values in memory, but the container idea can be helpful at first for visualizing.
	- In python, variables are declared when they are assigned. That is, they exist when you say they are equal to something.  
		```py
		name = "Jeanette"
		max = 100
		a = None
---
- **Functions** are repeatable sets of commands that can take input, can return output, and can have side effects. *Repeatable* is a key aspect of functions and a major reason that we write them. Functions package a set of commands together, so they can be called with one line. The *signature* of a function is the line in which it is defined. It always ends with a colon(:), and the contents of the function are indented. 
	- The simplest possible function is this:

	```py 
	def do_nothing():
		pass
	```
	This function is syntactically correct Python, so it runs when called,  but the function takes no input, returns no output, and has no side effects.
	- In order for functions to run, we must call them by name. A function merely being defined doesn't cause anything to happen. _The actions in the function happen when the function is called_. We would call the above function like this:
	```py
	do_nothing()
	```
	And I would expect to see no output.
	Note that I can call a function in the Python shell, where I see the `>>>` prompt, or I can call the function within a bigger Python program, a file with the extension `.py`. If I want to run that program, in the terminal I would run
	> `python my_program.py`
---
- **Parameters** are placeholders in the signature line of a function, in anticipation of input. When the function is called, actual _arguments_ are passed and assigned to the placeholder tags. The function then does what it is instructed to do with the input. For example, if we have a function called `double` that's meant to return double a number, we would write it like this:
	```py
	def double(number):
		double_number = 2 * number
		print(f"Twice your number is {double_number}.")
		return double_number
	```
	Why are `print` and `return` both there? `print` shows values in the terminal for humans to read, `return` makes values accessible in the computer's memory, so `print` is for people, and `return` is for the code.

- When we want to call the function and pass an **argument**, for example, the integer 5, we do this:
	```py
	double(5)
	```
	and we see this in the terminal:
	```py
	Twice your number is 10.
	```
	- What would you see if you called the function on -3? How about if we passed a string like "word?"
---

