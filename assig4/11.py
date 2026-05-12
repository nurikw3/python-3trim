import re


def is_valid_email(email):
    return bool(re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email))


email = input("enter your email: ")

print(is_valid_email(email))
