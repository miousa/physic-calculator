import sys
sys.path.append('.')

from utils import get_positive_float, get_nonnegative_float, get_float
import math

G = 9.8

def kinetic_energy():
     m = get_positive_float("Mass (kg): ")
     v = get_nonnegative_float("Speed (m/s): ")
     print(f"Kinetic energy = {m * v ** 2 / 2:.2f} J")
     
def potential_energy():
    m = get_positive_float("Mass (kg): ")
    h = get_nonnegative_float("Height (m): ")
    print(f"Potential energy = {m * G * h:.2f} J")
    
def work():
    f = get_float("Force (N): ")
    s = get_nonnegative_float("Path (m): ")
    angle = get_float("Enter angle (degrees): ")
    rad = math.radians(angle)
    print(f"Mechanical work = {f * s * math.cos(rad):.2f}")
    
def efficiency():
    a_useful = get_nonnegative_float("Enter useful work (J): ")
    a_total = get_positive_float("Enter total work (J): ")
    print(f"Efficiency = {(a_useful / a_total) * 100:.2f} %")
    
def menu():
    while True:
        print("\n--- CONSERVATION LAWS ---")
        print("1. Kinetic energy (E_k = mv²/2)")
        print("2. Potential energy (E_p = mgh)")
        print("3. Work (A = F·S·cosα)")
        print("4. Efficiency (η = A_useful / A_total · 100%)")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1": kinetic_energy()
        elif choice == "2": potential_energy()
        elif choice == "3": work()
        elif choice == "4": efficiency()
        elif choice == "0": return
        else: print("Invalid input!")
            