def life_in_weeks(your_age):
    year_in_weeks = 52
    lifetime = 90 - your_age
    expected_in_weeks = lifetime * year_in_weeks
    print(f"You have {expected_in_weeks} weeks left.")
    
life_in_weeks(45)