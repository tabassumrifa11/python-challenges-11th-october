print("\033c")

import random
import string

def generate_password(length):
    if length < 6:
        return "Password length must be at least 6 characters!"

    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    
    password = [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_chars = lower_case + upper_case + digits + special_chars
    password = random.choices(all_chars, k=length - len(password))
    
    random.shuffle(password)

    return ''.join(password)

password_length = random.randint(6, 12)
password = generate_password(password_length)

print(f"Generated Password: {password}")