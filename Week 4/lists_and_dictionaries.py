bands = ["Jimmy Eat World", "Queen", "Andrew Bird", "The Band", "Led Zeppelin", 123, "The Band"]
               # 0              1          2             3           4           5       6
# print(len(bands))

# # append
# print(bands.append("Mac Miller"))
# # print(bands)
# # remove
# print(bands.remove("Led Zeppelin"))
# # print(bands)
# # insert
# print(bands.insert(4, "Led Zeppelin"))
# # print(bands)
# # pop
# print(bands.pop())
# # print(bands)
# print(bands.index("Queen"))
# # print(bands)
# bands[3] = "Billie Eilish"
# print(bands)

# # provides index position and value at that index
# for index in range(len(bands)):
#     print(index, bands[index])

# # provides only the value
# for band in bands:
#     print(band)

# makes a copy of bands and checks for bad data, 
# make it a function
def remove_non_string_data(list_of_stuff):
    cleaned_list = list_of_stuff.copy()
    for index in range(len(list_of_stuff)):
        print(f'We are currently at list_of_stuff[{index}]')
        print(type(list_of_stuff[index]))
        if not isinstance(list_of_stuff[index], str):
            cleaned_list[index] = 'BAD'
    print(cleaned_list)

cheeses = ['mozzarella', 'pepper jack', False, 'vegan cheese', 'cheddar']

# remove_non_string_data(cheeses)

bands = ["Jimmy Eat World", "Queen", "Andrew Bird", "The Band", "Led Zeppelin", 123, "The Band",]

# dictionary where the keys are the and names and the values are info
bands_dict = {
    "Jimmy Eat World":{"members": 5},
    "Queen": {"members": 4},
    "Andrew Bird": {"members": 1},
    "The Band": {"members": 4},
    "Led Zeppelin": {"members": 4},
}

# add a band to this dictionary

bands_dict["Mac Miller"] = {"members": 1}

# obtain values by doing Name_of_dict["key"]
print(f'The band "Led Zeppelin" has {bands_dict["Led Zeppelin"]["members"]} members.')





