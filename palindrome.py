def is_palindrome(number):
    # Convert the number to a string
    str_number = str(number)
    # Check if the string is equal to its reverse
    return str_number == str_number[::-1]

# User input
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
