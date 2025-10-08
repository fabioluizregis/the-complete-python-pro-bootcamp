capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# Nested list in Dictionary

travel_log = {
    "France" : ["Paris", "Little", "Dijon"],
    "Germany" : ["Stuggart", "Berlin"]
}

# print Little

print(travel_log["France"][1])


# Nested List
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])


travel_log_again = {
    "France" : {
        "num_times_visited" : 8,
        "cities_visited" : ["Paris", "Little", "Dijon"]
    },
    "Germany" : {
        "num_times_visited" : 5,
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"]
    }
}

print(travel_log_again["Germany"]["cities_visited"][2])