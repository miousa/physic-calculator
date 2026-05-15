from . import heating
from . import combustion
from . import phase_transitions

def main_menu():
    while True:
        print("\n--- THERMODYNAMICS ---")
        print("1. Heating")
        print("2. Combustion")
        print("3. Phase transitions")
        print("0. Back")
        
        choice = input("Choose")
        
        if choice == "1":
            heating.menu()
        elif choice == "2":
            combustion.menu()
        elif choice == "3":
            phase_transitions.menu()
        elif choice == "0":
            break
        else:
            print("Invalid input!")