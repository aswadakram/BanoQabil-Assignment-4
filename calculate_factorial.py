user_num = int(input("Enter a positive integer: "))

if user_num < 0:
    print("Invalid integar! Enter a positive integer.")
else:
    factorial = 1
    for i in range(1, user_num + 1):
        factorial *= i
    print("The factorial of", user_num, "is", factorial)
