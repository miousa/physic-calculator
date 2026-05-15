from mechanics.menu import main_menu
from electricity.menu import main_menu
from optics.menu import main_menu
from thermodynamics.menu import main_menu

def main():
    while True:
        print("\n=== PHYSICS CALCULATOR ===")
        print("1. Mechanics")
        print("2. Electricity")
        print("3. Optics")
        print("4. Thermodynamics")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            main_menu()
        elif choice == "2":
            main_menu()
        elif choice == "3":
            main_menu()
        elif choice == "4":
            main_menu()
        elif choice == "0":
            break
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()