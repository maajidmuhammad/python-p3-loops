
#!/usr/bin/env python3
import time



def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        time.sleep(1)  # Add a delay of 1 second
        countdown -= 1
    print("Happy New Year!")

# Call the function to run it
happy_new_year()


def square_integers(int_list):
    # code goes here!
    squared_list = []
    for num in int_list:
        squared_list.append(num ** 2)
    return squared_list

# Example usage:
result = square_integers([2, 3, 4])
print(result)  


def fizzbuzz():
    # code goes here!
    for num in range(1,101):
        if num%3==0 and  num%5==0:
            print("FizzBuzz")
        elif num%3==0:
            print("Fizz")
        elif num%5==0:
            print("Buzz") 
        else:
            print(num)
    
fizzbuzz()               
