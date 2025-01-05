# script3.py
import random

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    print(f"Here is a random number for you: {generate_random_number()}")
