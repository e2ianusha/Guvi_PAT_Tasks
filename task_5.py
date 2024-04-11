#Expected Output for the Given Python Code:
#The provided Python code filters the elements in the data list using a lambda function. It retains only those elements that are greater than 4.
#The expected output is a list containing the filtered elements: [10, 501, 22, 37, 100, 999, 87, 351].

# Python Code to Check if Each Element in a List Is a String or an Integer
data = [10, 501, 22, 37, 100, 999, 87, 351, "hello", "world", 42]
result = list(map(lambda x: "string" if isinstance(x, str) else "integer", data))
print(result)

# Creating a Fibonacci Series Using a Python Lambda Function
def generate_fibonacci(n):
    fibonacci_series = [0, 1]
    while len(fibonacci_series) < n:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)
    return fibonacci_series

n = 50  # Number of elements in the Fibonacci series
fibonacci_series = generate_fibonacci(n)
print(fibonacci_series)



# Python Function to Validate Regular Expressions
#Email address validation
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Example usage:
email_to_check = "example@email.com"
print(validate_email(email_to_check))  # True if valid, False otherwise

# Mobile Numbers of Bangladesh
def validate_bangladesh_mobile_number(number):
    pattern = r'^\+8801[0-9]{9}$'
    return re.match(pattern, number) is not None

# Example usage:
bd_mobile_number = "+8801712345678"
print(validate_bangladesh_mobile_number(bd_mobile_number))  # True if valid, False otherwise

#Telephone Numbers of USA:
def validate_usa_telephone_number(number):
    pattern = r'^\(\d{3}\)\s?\d{3}-\d{4}$'
    return re.match(pattern, number) is not None

# Example usage:
usa_telephone = "(123) 456-7890"
print(validate_usa_telephone_number(usa_telephone))  # True if valid, False otherwise

#16-Character Alpha-Numeric Password:
def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return re.match(pattern, password) is not None

# Example usage:
user_password = "Abcd1234!@#$5678"
print(validate_password(user_password))  # True if valid, False otherwise
