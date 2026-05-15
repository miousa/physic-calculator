import sys
sys.path.append('.')

from utils import get_positive_float, get_float, get_nonnegative_float

def joule_lenz_current():
    i = get_float("Enter Current strength (A): ")
    r = get_positive_float("Enter resistance (Ω): ")
    t = get_nonnegative_float("Enter time (s): ")
    print(f"Energy lenz = {i ** 2 * r * t:.2f} J")

def joule_lenz_voltage():
    u = get_float("Enter voltage (V): ")
    r = get_positive_float("Enter resistance (Ω): ")
    t = get_nonnegative_float("Enter time (s): ")
    print(f"Voltage lenz = {(u ** 2 / r) * t:.2f} J")
    
def menu():
    while True:
        print("\n--- HEAT ---")
        print("1. Current joul lenz (Q=I²·R·t)") 
        print("2. Voltage joul lenz (Q=U^2/R·t)") 
        print("3. Back")
        
        choice = input("Choose: ")
        
        if choice == "1": joule_lenz_current()
        elif choice == "2": joule_lenz_voltage()
        elif choice == "3": return
        else: print("Invalid input!") 
        

