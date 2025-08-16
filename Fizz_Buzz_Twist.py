for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0 and i % 7 == 0:
            print("FizzBuzzBang")
        elif i % 5 == 0:
            print("FizzBuzz")
        elif i % 7 == 0:
            print("FizzBang")
        else:
            print("Fizz")
    elif i % 5 == 0:
        if i % 7 == 0:
            print("BuzzBang")
        else:
            print("Buzz")
    elif i % 7 == 0:
        print("Bang")
    else:
        continue