import sys
sys.path.append('.')

from utils import get_positive_float, get_float, get_nonnegative_float

def request_resistance():
    r1 = get_positive_float("Enter resistance r1 (Ω): ")
    r2 = get_positive_float("Enter resistance r2 (Ω): ")
    return r1, r2

def request_resistances():
    n = int(input("Enter number of resistors: "))
    resistances = []
    
    for i in range(n):
        r = get_positive_float(f"Enter resistance R{i+1} (Ω): ")
        resistances.append(r)
    return resistances
    
def series_two():
    r1, r2 = request_resistance()
    print(f"Total resistance = {r1 + r2:.2f} Ω")
    
def parallel_two_general():
    r1, r2 = request_resistance()
    r_tot = 1/r1 + 1/r2
    print(f"Total resistance = {1/r_tot:.2f} Ω")
    
def parallel_two_simple():
    r1, r2 = request_resistance()
    print(f"Total resistance = {(r1 * r2) / (r1 + r2)} Ω")   

def parallel_several():
    resistances = request_resistances()
    total_inverse = 0
    
    for r in resistances:
        total_inverse += 1 / r
    print(f"Total resistance = {1 / total_inverse:.2f} Ω")
    
def menu():
    while True:
        print("\n--- CIRCUITS ---")
        print("1. Series (two resistors)")
        print("2. Parallel (two resistors, general formula)")
        print("3. Parallel (two resistors, simplified formula)")
        print("4. Parallel (three or more resistors)")
        print("5. Back")
        
        choice = input("Choose: ")
        
        if choice == "1": series_two()
        elif choice == "2": parallel_two_general()
        elif choice == "3": parallel_two_simple()
        elif choice == "4": parallel_several()
        elif choice == "5": return 
        else: print("Invalid input!")
   




    

        
    
    