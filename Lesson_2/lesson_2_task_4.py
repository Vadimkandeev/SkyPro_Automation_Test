def cycle(x): # Добавлена функция цикла, которая вызывается
    for i in range(1, x+1):  # в условном операторе
        print(i)


def fizz_buz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        cycle(num) # <<--
        print("FizzBuzz")
    elif num % 3 == 0:
        cycle(num) # <<--
        print("Fizz")
    elif num % 5 == 0:
        cycle(num) # <<--
        print("Buzz")


fizz_buz(int(input()))
