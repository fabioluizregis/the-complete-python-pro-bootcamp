# problem with 1994 not printing anything

### ORIGINAL CODE

# year = int(input("What`s your year of birth? : "))

# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z")

### FIXED CODE

year = int(input("What`s your year of birth? : "))

if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z")