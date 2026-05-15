from . import lenses

def main_menu():
     while True:
        print("\n=== OPTICS ===")
        print("1. Lenses")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1":
            lenses.menu()
        elif choice == "0":
            break
        else:
            print("Invalid input!")