
######## Original Code ########

# age = int(input("How old are you? : "))
# if age > 18:
# print("You can dreive at age {age}")

######## First error Fix ########

# age = int(input("How old are you? : "))
# if age > 18:
#     print("You can dreive at age {age}")

######## Second error Fix ########

# age = int(input("How old are you? : "))
# if age > 18:
#     print(f"You can dreive at age {age}")

######## Third error Fix ########

try:
    age = int(input("How old are you? : "))
except ValueError:
    print("You have typed an invalid number. Please try again with a numerical response sucha as 15.")
if age > 18:
    print(f"You can dreive at age {age}")