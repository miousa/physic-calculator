import sys
sys.path.append('..')

from utils import get_positive_float, get_nonnegative_float, get_float

def lens_formula():
    d = get_positive_float("Enter the distance from the object to the lens (m): ")
    f = get_positive_float("Enter the distance from the lens to the image (m): ")
    print(f"Focal length = {(d * f) / (d + f):.2f} m")
    
def optical_power():
    foc = get_positive_float("Enter focal length (m): ")
    print(f"Optical power = {1 / foc:.2f}")
    
def menu():
    while True:
        print("\n--- LENSES ---")
        print("1. Focal length (1/F = 1/d + 1/f)")
        print("2. Optical power (D = 1/F)")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1": lens_formula()
        elif choice == "2": optical_power()
        elif choice == "0": return
        else: print("Invalid input!")
        
