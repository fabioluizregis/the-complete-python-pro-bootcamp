### ORIGINAL CODE

# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")


#### FIXED CODE

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()

# Describe the Problem - Write your answers as comments:
    # 1- What is the for loop doing?
    #     It is iterating from 1 to 20. But 20 is not included on the Loop. Loop shall finish at 19

    # 2- When is the function meant to print "You got it"?
    #     When the i variable from iteration get to the value 20, that will never happen

    # 3- What are your assumptions about the value of i?
    #     It is iterating correctly but the range is wrong to make the print happen