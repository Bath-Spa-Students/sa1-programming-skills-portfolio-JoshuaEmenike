def is_even_or_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

def main():
    num = int(input("Enter a number: "))  # Get user input
    result = is_even_or_odd(num)  # Check if it's even or odd
    print(result)  # Print the result

if __name__ == "__main__":
    main()
