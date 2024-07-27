user_num = int(input("Enter a positive integer: "))

if user_num < 0:
    print("Invalid integar! Enter a positive integer.")
else:
    result = 1
    for i in range(1, user_num + 1):
        result *= i
    print("The factorial of", user_num, "is", result)
