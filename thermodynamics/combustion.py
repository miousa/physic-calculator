import sys 
sys.path.append('..')

from utils import get_float, get_nonnegative_float, get_positive_float

def combustion():
    q = get_nonnegative_float("Enter specific heat of combustion (J/kg): ")
    m = get_nonnegative_float("Enter mass of substance (kg): ")
    print(f"The amount of heat(combustion) = {q * m:.2f} J")
    
def menu():
    while True:
        print("\n--- COMBUSTION ---")
        print("1. Combustion (Q=q⋅m)")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1": combustion()
        elif choice == "0": return
        else: print("Invalid input!")
        
