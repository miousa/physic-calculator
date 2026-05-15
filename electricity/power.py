import sys
sys.path.append('.')

from utils import get_positive_float, get_float, get_nonnegative_float

def power_voltage_current():
    u = get_float("Enter voltage (V): ")
    i = get_float("Enter Current strength (A): ")
    print(f"Power = {u * i:.2f} W")
    
def power_voltage_resistance():
    u = get_float("Enter voltage (V): ")
    r = get_positive_float("Enter resistance (Ω): ")
    print(f"Power resistance = {u ** 2 / r:.2f} W")
    
def power_current_resistance():
    i = get_float("Enter Current strength (A): ")
    r = get_positive_float("Enter resistance (Ω): ")
    print(f"Power current = {i ** 2 * r:.2f} W")
    
def work_energy():
    p = get_nonnegative_float("Enter power (W): ")
    t = get_nonnegative_float("Enter time (s): ")
    print(f"Energy work = {p * t:.2f}")
    
def menu():
    while True:
        print("\n--- POWER & WORK ---")
        print("1. Power (P = U*I)")
        print("2. Power (P = U²/R)")
        print("3. Power (P = I²·R)")
        print("4. Work (A = P·t)")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1": power_voltage_current()
        elif choice == "2": power_voltage_resistance()
        elif choice == "3": power_current_resistance()
        elif choice == "4": work_energy()
        elif choice == "0": return
        else: print("Invalid input!")
    
