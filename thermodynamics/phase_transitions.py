import sys
sys.path.append('..')

from utils import get_float, get_nonnegative_float, get_positive_float

def melting_freezing():
    λ = get_nonnegative_float("Enter specific heat of melting (J/kg): ")
    m = get_nonnegative_float("Enter mass of substance (kg): ")
    print(f"Amount of heat(melting/crystallization) = {λ * m:.2f} J")
    
def vaporization_condensation():
    l = get_nonnegative_float("Enter specific heat of vaporization (J/kg)")
    m = get_nonnegative_float("Enter mass of substance (kg): ")
    print(f"Amount of heat (vaporization/condensation) = {l * m:.2f} J")

def menu():
    while True:
        print("\n--- PHASE TRANSITIONS ---")
        print("1. Melting freezing (Q=λ⋅m)")
        print("2. Vaporization/condensation (Q=l⋅m)")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1": melting_freezing()
        elif choice == "2": vaporization_condensation()
        elif choice == "0": return
        else: print("Invalid input!")
    