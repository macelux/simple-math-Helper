import math


def print_hi(message):
    print(f'Hi, {message}')


def factorial(number):
    return math.factorial(number)


def log(number):
    return math.log(number)


def sqrt(number):
    return math.sqrt(number)


if __name__ == '__main__':
    print_hi('Hi, Welcome to simple math helper')
    print('What would you like to calculate?')
    print("1. Square root \n2. log \n3. Factorial")

    try:
        option = int(input("Enter a number: "))
        user_selection = ("Square root", "log", "factorial")

        if 1 <= option <= 3:
            user_option = option - 1
            number_to_calculate = float(input(f"\nEnter the number to find the {user_selection[user_option]}:  "))
            if option == 1:
                result = sqrt(number_to_calculate)
                print(f"\n\nThe {user_selection[user_option]} of {number_to_calculate} is : {int(result)}")
            elif option == 2:
                result = log(number_to_calculate)
                print(f"\n\nThe {user_selection[user_option]} of {number_to_calculate} is : {result}")
            else:
                result = factorial(number_to_calculate)
                print(f"\nThe {user_selection[user_option]} of {number_to_calculate} is : {int(result)}")
        else:
            print('wrong selection. Please re run the program')

    except ValueError:
        print('Not a number! Please re run the program')
