# Python Notebooks: The Force Awakens
## Condensed prequel to the Python Notebooks

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
## How We Represent Data in Python

- We've seen how we represent numbers, text, and True/False as well as the idea of variables. What happens if we want to represent a collection in Python? The data types we will use most often for that are **lists**, **tuples**, and **dictionaries**. Additional specialized data types can be found in the [documentation](https://docs.python.org/3/library/datatypes.html).

---
- **Lists** are useful for demonstrating collections of items and are enclosed in square brackets `[]`. They can be items of the same type or different types. Can you have a list of lists? Sure. Lists, as all other data types, can be assigned as values to variables. For example:
```py
	# list of strings represented by the variable, `flavors`
	flavors = ["chocolate", "Cherry Garcia", "vanilla"]
	# list of tuples represented by the variable `scores`
	scores = [("UNC", 98), ("Duke", 89)]
	# list of dictionaries represented by the variable `bands`
	bands = [
	{"Foo Fighters": {
		"Dave Grohl": ("guitar", "lead vocals"), 
		"Pat Smear": "guitar",
		"Chris Shiflett": ("guitar", "backing vocals"),
		"Nate Mendel": "bass",
		"Taylor Hawkins": ("drums", "percussion", "backing vocals"),
		"Rami Jaffee": ("keyboard", "piano"),
		}
	},
	{"Nickelback": {
		"Chad Kroeger": ("lead vocals", "lead guitar"),
		"Ryan Peake": ("rhythm guitar", "backing vocals", "keyboard"),
		"Mike Kroeger": "bass",
		"Daniel Adair": ("drums", "percussion", "backing vocals"),
		}
	}]
	# list of various types of objects
	various = ["A WORD", 6, False, -25.0, ("a", "tuple")]
```
---
Lists are ordered, that is, every item has its place in line, called its **index**,
like picking a number at the deli or the DMV. The numbers start at 0, the far left item in the list.  
```py	
	animals = ["zebra", "pika", "octopus", "black bear"]
    #             ↑		   ↑        ↑            ↑
	# index		  0        1        2            3
```

We can retrieve items from a list using its _index_, like this:
```py
	> animals[2]
	> "octopus"

```
We can also _slice_ a list, obtaining a segment of the list with indexes, `[start:stop]`, which is non-inclusive, meaning we get the item right before the stop index, but not the one at the stop index. If no start is given, the default value is 0. If no stop is given, the default value is the length of the list (the last index position + 1).
```py
	> animals[1:3]
	>['pika', 'octopus']

```
We can change the value at a given index like this:
```py
   animals[3] = "orangutan"
   # now look at the list 
   > animals
   > ["zebra", "pika", "octopus", "orangutan"]
```
---
Python provides a number of **built-in methods for lists**. Using the following list
as an example, let's look at several of the methods we will use most often:
```py
colors = ["red", "green", "blue", "purple", "yellow"]
# list.pop() removes and returns the last item in the list
> colors.pop()
> 'yellow'
> colors
> ["red", "green", "blue", "purple"]
# list.append() adds an item to the end of the list
> colors.append("orange")
> colors
> ["red", "green", "blue", "purple", "orange"]
# len() is a built-in Python function, not limited to lists, that tells us the number of items in an object
> len(colors)
> 5
# in is another built-in function that can be used on lists to check
```
#### The rest of the `list` methods can be found in the [Python docs](https://docs.python.org/3/tutorial/datastructures.html). 
--- 
**Tuples**, which rhyme with "pupils" or "couples", depending on who you ask, are similar to lists and are enclosed in parentheses `()`. Tuples are _iterable_, like lists, meaning they have items in an indexed order that can be iterated (looped) through. The major difference between tuples and lists is that tuples are _immutable_, cannot be changed.  

You can obtain items from a tuple by its index, as we did with lists:
```py
> colors_tuple = ("red", "green", "blue", "purple", "orange")
> colors_tuple[3] = "purple"
```
#### But we can't reassign values because tuples cannot be changed.  
---
**Dictionaries** are key: value pairs, Python's version of the concept of _hash tables_. As with Webster's Dictionary, where you look up definitions by the word, you can look up values by their keys in Python dictionaries. Keys and values can be almost any data type, except: _keys can only appear once in a dictionary, and keys must be of an immutable type (no lists or dictionaries)_. Values can repeat any number of times in a dictionary and can be of any type. Note that dictionaries *do not* have indexes. They do (as of version 3.6) retain the order that items were inserted, but we don't use indexes to retrieve or update information.
```py
	foo_fighters = {
		"Dave Grohl": ("guitar", "lead vocals"), 
		"Pat Smear": "guitar",
		"Chris Shiflett": ("guitar", "backing vocals"),
		"Nate Mendel": "bass",
		"Taylor Hawkins": ("drums", "percussion", "backing vocals"),
		"Rami Jaffee": ("keyboard", "piano"),
		}
# to obtain what Dave Grohl plays in Foo Fighters (now, not the first album where he played everything), we can use the key to find the value.
> foo_fighters["Dave Grohl"]
> ('guitar', 'lead vocals')
# if we want to update a dictionary, as in the case where the young drumming prodigy Nandi Bushell, who owned Dave Grohl in an Internet drum battle, joins the band as another drummer, we add key:value pairs to a dictionary by assigning a value to the new key.
> foo_fighters["Nandi Bushell"] = "more awesome drums"
# our dictionary has been updated
> foo_fighters
> {
	"Dave Grohl": ("guitar", "lead vocals"), 
	"Pat Smear": "guitar",
	"Chris Shiflett": ("guitar", "backing vocals"),
	"Nate Mendel": "bass",
	"Taylor Hawkins": ("drums", "percussion", "backing vocals"),
	"Rami Jaffee": ("keyboard", "piano"),
	"Nandi Bushell": "more awesome drums",
}
# Let's say this causes Taylor Hawkns to become disgruntled and quit. We can update his entry like this:
> foo_fighters["Taylor Hawkins"] = "retired"
# Now our dictionary shows his new status
> foo_fighters
> {
	"Dave Grohl": ("guitar", "lead vocals"), 
	"Pat Smear": "guitar",
	"Chris Shiflett": ("guitar", "backing vocals"),
	"Nate Mendel": "bass",
	"Taylor Hawkins": "retired",
	"Rami Jaffee": ("keyboard", "piano"),
	"Nandi Bushell": "more awesome drums",
}
```
---
Lists, dictionaries, and tuples are **iterable**, meaning we can loop through them, performing tasks on each item one at a time. If we are looping through a dictionary, we have to decide whether we want to loop through the `keys()`, `values()`, or `items()`. The if statement will catch the member of the group who does not play an instrument anymore. `items()` gives us each key:value pair as a tuple, and we can access the items in that tuple by index.
```py
	for person in foo_fighters.items():
		if person[1] != "retired":
			print(f'{person[0]} plays {person[1]}')
```
