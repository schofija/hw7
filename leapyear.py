def check(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return 0
            
        return True

    return False
