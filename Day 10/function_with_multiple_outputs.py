def format_name(first_name, last_name):
    return f"{last_name.title()}, {first_name.title()}"

print(format_name("gRaVE", "diGGer"))

########################################################################

def cat_name(first_name, second_name):
    final_name = second_name.title() + ", " + first_name.title()
    return final_name

my_cat_name = cat_name("jhOnnY", "walkeR")
print(my_cat_name)