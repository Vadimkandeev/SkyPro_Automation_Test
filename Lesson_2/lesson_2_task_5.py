def month_to_season(month):
    if (1 <= month < 3) or month == 12: # Внесено исправление
        print("Winter")
    elif 3 <= month <= 5:
        print("Spring")
    elif 6 <= month <= 8:
        print("Summer")
    elif 9 <= month <= 11:
        print("Fall")

month_to_season(int(input()))