from . import kinematics
from . import dynamics
from . import statics
from . import conservation

def main_menu():
    while True:
        print("\n=== MECHANICS ===")
        print("1. Kinematics")
        print("2. Dynamics")
        print("3. Statics")
        print("4. Conservation")
        print("0. Back")
        
        choice = input("Choose: ")

        if choice == "1":
            kinematics.menu()
        elif choice == "2":
            dynamics.menu()
        elif choice == "3":
            statics.menu()
        elif choice == "4":
            conservation.menu()
        elif choice == "0":
            break
        else:
            print("Invalid input!")