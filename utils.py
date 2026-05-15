def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive!")
                continue
            return value
        except ValueError:
            print("Enter a number!")

def get_nonnegative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative!")
                continue
            return value
        except ValueError:
            print("Enter a number!")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a number!")
            
            
            
