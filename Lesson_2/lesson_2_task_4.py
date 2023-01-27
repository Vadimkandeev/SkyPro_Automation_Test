def fizz_buz(num):
    if (int(num) % 3 == 0) and (int(num) % 5 == 0):
        print("FizzBuzz")
    elif int(num) % 3 == 0:
        print("Fizz")
    elif int(num) % 5 == 0:
        print("Buzz")
     
fizz_buz(input())