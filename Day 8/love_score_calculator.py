def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    loweer_names = combined_names.lower()
    
    t = loweer_names.count("t")
    r = loweer_names.count("r")
    u = loweer_names.count("u")
    e = loweer_names.count("e")
    first_digit = t + r + u + e
    
    l = loweer_names.count("l")
    o = loweer_names.count("o")
    v = loweer_names.count("v")
    e = loweer_names.count("e")
    second_digit = l + o + v + e 
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
    
calculate_love_score("Kanye West", "Kim Kardashian")