colours = {
    "apple" : "red",
    "pear" : "green",
    "banana" : "yellow"
}

print(colours["pear"])

colours["orange"] = "orange"

print(colours)


empty_dictionary = {}

# Wipe an existing dictionary
# colours = {}
# print(colours)

# Edit an item in a dictionary
# colours["pear"] = "Not green anymore"
# print(colours)

# Loop through a dictionary
for key in colours:
    print(key)
    print(colours[key])