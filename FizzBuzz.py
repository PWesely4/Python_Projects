num = 0
while num < 100:
    num += 1
    if num % 3 == 0:
        if num % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif num % 5 == 0:
        if num % 3 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(num)