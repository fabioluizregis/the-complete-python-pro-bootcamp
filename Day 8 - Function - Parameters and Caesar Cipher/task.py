def greet():
    print("Hello World!")
    print("This is a Python code..")
    print("Enjoy the process")

greet()

def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"This is a Python code {name}..")
    print(f"Enjoy the process {name}")

greet_with_name("Fabio")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Fabio", "Araçoiaba da Serra")