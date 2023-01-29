def cycle(x): # Добавлена функция цикла, которая вызывается
    for i in range(1, x+1):  # в условном операторе
        print(i)


def fizz_buz(num):
    if (int(num) % 3 == 0) and (int(num) % 5 == 0):
        cycle(int(num))
        print("FizzBuzz")
    elif int(num) % 3 == 0:
        cycle(int(num))
        print("Fizz")
    elif int(num) % 5 == 0:
        cycle(int(num))
        print("Buzz")


fizz_buz(input())
