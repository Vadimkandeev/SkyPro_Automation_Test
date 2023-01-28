sum = int(input())
years = int(input())
def bank(x, y):
    for i in range(y):
        x = x + x/10
    #print(x)
    print(round(x, 2)) # Лучше использовать функцию округления результата до двух знаков 
bank(sum, years)       # после запятой
