# "Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”

for n in range(1, 101):
    x = 3 # To quickly change what multiples show 'Fizz'
    y = 5 # To quickly change what multiples show 'Buzz'
    if n % x == 0 and n % y == 0:
        print("FizzBuzz")
    elif n % x == 0:
        print ("Fizz")
    elif n % y == 0:
        print("Buzz")
    else:
        print(n)
