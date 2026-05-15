import sys
sys.path.append('.')

from utils import get_positive_float, get_float

RESISTIVITY = {
    "silver": 0.016,
    "copper": 0.017,
    "gold": 0.024,
    "aluminum": 0.028,
    "zinc": 0.059,
    "brass": 0.07,
    "bronze": 0.095,
    "iron": 0.10,
    "constantan": 0.50,
    "nichrome": 1.1
}

def cur_strength():
    u = get_float("Enter voltage (V): ")
    r = get_positive_float("Enter resistance (Ω): ")
    print(f"Current strength = {u / r:.2f} A")
    
def calc_voltage():
    r = get_positive_float("Enter resistance (Ω): ")
    i = get_float("Enter Current strength (A): ")
    print(f"Voltage = {i * r:.2f} V")
    
def calc_resistance():
    u = get_float("Enter voltage (V): ")
    i = get_float("Enter current strength (A): ")
    print(f"Resistance = {u / i:.2f} Ω")
    
def resistance_by_material():
    print("\nAvailable materials (ρ in Ω·mm²/m):")
    for name, value in RESISTIVITY.items():
        print(f"  {name}: {value}")
        
    material = input("Enter material: ").lower()
    
    if material in RESISTIVITY:
        rho = RESISTIVITY[material]
    else:
        print(f"Material '{material}' not found. Please enter resistivity manually.")
        rho = get_positive_float("Enter resistivity ρ (Ω·mm²/m): ")
    return rho   

def conductor_res():
    rho = resistance_by_material() 
    l = get_positive_float("Enter length (m): ")
    s = get_positive_float("Enter cross-sectional area (mm²): ")
    print(f"Conductor resistance = {rho * l / s:.3f} Ω")
          
def menu():
    while True:
        print("\n--- OHM'S LAW ---")
        print("1. Current (I = U/R)")
        print("2. Voltage (U = I*R)")
        print("3. Resistance (R = U/I)")  
        print("4. Conductor resistance (R = ρ·l/S)")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1": cur_strength()
        elif choice == "2": calc_voltage()
        elif choice == "3": calc_resistance()
        elif choice == "4": conductor_res()
        elif choice == "0": return
        else: print("Invalid input!")
        

        

              
          
