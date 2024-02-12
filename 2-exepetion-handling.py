#dividing to input numbers, if it is a valid int it will a error(ValueError).
def divide_numbers():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        result = numerator / denominator
        print(f"The result of division is: {result}")
    except ValueError:
        print("Please enter valid integers.")
   

if __name__ == "__main__":
    divide_numbers()
