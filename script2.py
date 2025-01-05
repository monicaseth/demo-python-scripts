
# script2.py
def calculate_sum(a, b):
    return a + b

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum is: {calculate_sum(num1, num2)}")
    except ValueError:
        print("Please enter valid numbers!")
