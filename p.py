import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Generate and print 150,000 characters
print(generate_random_string(150000))  # Fixes #19
