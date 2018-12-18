# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

number = int(input("Enter your number:"))

rangeOfNumberList = list(range(1, number+1))

listOfDivisors = []

for i in rangeOfNumberList:
    if number % i == 0:
        listOfDivisors += [i]

print(listOfDivisors)