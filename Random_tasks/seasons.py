def get_season(num):
    if num in {12, 1, 2}:
        return 'winter'
    elif num in {3, 4, 5}:
        return 'spring'
    elif num in {6, 7, 8}:
        return 'summer'
    elif num in {9, 10, 11}:
        return 'autumn'
    else:
        return 'число не входит в 1-12'

print(get_season(5))