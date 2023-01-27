"""
sum = 0

def bank(x, y):
    sum = int(x)
    for i in range(int(y)+1):
        sum = sum + sum/10

a = input(int())
b = input(int())
bank(a, b)
print(sum)
"""
sum = 0
a = input()
b = input()
def func(x, y):
    sum = x + y
    return sum
print(sum)

func(a, b)   