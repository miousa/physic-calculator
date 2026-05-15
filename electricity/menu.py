from . import ohms_law
from . import heat
from . import power
from . import circuits

def main_menu():
    while True:
        print("\n=== ELECTRICITY ===")
        print("1. Ohm's law")
        print("2. Power and work (soon)")
        print("3. Joule–Lenz law (soon)")
        print("4. Circuits (soon)")
        print("0. Back")

        
        choice = input("Choose: ")
        
        if choice == "1":
            ohms_law.menu()
        elif choice == "2":
            power.menu()
        elif choice == "3":
            heat.menu()
        elif choice == "4":
            circuits.menu()
        elif choice == "0":
            break
        else:
            print("Invalid input!")
            
            
