import sys
sys.path.append('..')

from utils import get_float, get_nonnegative_float, get_positive_float

def heating_cooling():
    c = get_nonnegative_float("Enter specific heat (J/kg): ")
    m = get_nonnegative_float("Enter mass (kg): ")
    d_t = get_float("Enter temperature change: ")
    print(f"Amount of heat (heating/cooling) = {c * m * d_t:.2f} J")
    
def menu():
    while True:
        print("\n--- HEATING ---")
        print("1. Amount of heat (Q=c⋅m⋅Δt)")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1": heating_cooling()
        elif choice == "0": return
        else: print("Invalid input!")
        
        
      
            