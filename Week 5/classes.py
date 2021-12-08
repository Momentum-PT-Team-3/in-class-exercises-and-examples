# Warm Up - fix this function.

# This function is supposed to take a list of words and return a new 
# list with the one-letter words removed. It's not doing that. First,
# run the function with some test word lists to see what it is doing
# then fix it so it has the desired output.

def remove_short_words(word_list):
    long_words = []
    for word in word_list:
        if len(word) > 1:
            long_words.append(word)
    # print(long_words)
    return long_words

# make your own test lists to try it out
test_list = ["words", "are", "simple", "a", "cat", "I"]

remove_short_words(test_list)

# try to represent a musician with a dictionary

musicians = [{
    "name": "Andrew Bird", 
    "instrument": ["violin", "whistle"],
    "record label": "Merge",
    "bands" : []
    },
    {

    }]

# as we reach the limitations of dictionaries to represent data, we 
# can move to classes
# classes generally represent the nouns in our code, the people, places, and things

class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f'{self.name}: {self.instrument}'

# when I create an object that's an element of a class, it's called an instance
# let's create a musician and store that instance in a variable
# writing the name of the class with () causes the __init__ method to be called
snoop = Musician("Snoop Dogg", "MC")

print(snoop)

jewel = Musician("Jewel", "guitar")
print(jewel)

class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def __str__(self):
        return self.name

    @property
    def show_members(self):
        print(f'The members of {mouse_rat.name} are: ', [f"{member}" for member in mouse_rat.members])

mouse_rat = Band("Mouse Rat")
print(f'The members of {mouse_rat.name} are {mouse_rat.members}')

mouse_rat.members.extend([snoop, jewel])

print(f'The members of {mouse_rat.name} are: ', [f"{member}" for member in mouse_rat.members])
# create new musician instances
andy = Musician("Andy Dwyer", "guitar")
duke = Musician("Duke Silver", "saxophone")
# add those musician to the members of the band
new_members = [andy, duke]
mouse_rat.members.extend(new_members)
#print out the new band members
mouse_rat.show_members
# get values of attributes for new members
member_info_tuples = [("Laurell", "harmonica"), ("Vanessa", "drums"), ("Samuel", "piano")]

# create a musician instance for each new member
for member_tuple in member_info_tuples:
    name, instrument = member_tuple
    new_member = Musician(name, instrument)
    # add that new member to mouse_rat members
    mouse_rat.members.append(new_member)


mouse_rat.show_members
