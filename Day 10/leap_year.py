def is_leap_year(year):
    if year % 4 != 0:
        leap = False
    elif year % 4 == 0:
        if year % 100 != 0:
            leap = True
        elif year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = False
    else:
        leap = False
            
    return leap
    
print(is_leap_year(2400))
print(is_leap_year(1989))