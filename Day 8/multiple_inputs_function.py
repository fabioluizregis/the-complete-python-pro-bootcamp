def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")

# when information order matters
greet_with("Fabio","Araçoiaba da Serra")

# when information order does not matters
greet_with(location="Araçoiaba da Serra", name="Fabio")