import sys
sys.path.append('..') 

from utils import get_positive_float, get_float

G = 9.8

def pressure_solid():
    f = get_float("Force (N): ")
    s = get_positive_float("Area (m²): ")
    print(f"Pressure = {f / s:.2f} Pa")

def pressure_liquid():
    rho = get_positive_float("Density (kg/m³): ")
    h = get_positive_float("Depth (m): ")
    print(f"Pressure = {rho * G * h:.2f} Pa")

def archimedes_force():
    rho = get_positive_float("Fluid density (kg/m³): ")
    v = get_positive_float("Volume (m³): ")
    print(f"Archimedes force = {rho * G * v:.2f} N")

def density():
    m = get_positive_float("Mass (kg): ")
    v = get_positive_float("Volume (m³): ")
    print(f"Density = {m / v:.2f} kg/m³")

def menu():
    while True:
        print("\n--- STATICS ---")
        print("1. Solid pressure (p = F/S)")
        print("2. Liquid pressure (p = ρ·g·h)")
        print("3. Archimedes force (F_A = ρ·g·V)")
        print("4. Density (ρ = m/V)")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1": pressure_solid()
        elif choice == "2": pressure_liquid()
        elif choice == "3": archimedes_force()
        elif choice == "4": density()
        elif choice == "0": return
        else: print("Invalid input!")