import sys
sys.path.append('..')

from utils import get_positive_float, get_nonnegative_float, get_float

def speed():
    s = get_nonnegative_float("Path (m): ")
    t = get_positive_float("Time (s): ")
    print(f"Speed = {s / t:.2f} m/s")

def acceleration():
    v0 = get_float("Initial speed (m/s): ")
    v = get_float("Final speed (m/s): ")
    t = get_positive_float("Time (s): ")
    print(f"Acceleration = {(v - v0) / t:.2f} m/s²")

def path_with_acceleration():
    v0 = get_float("Initial speed (m/s): ")
    t = get_positive_float("Time (s): ")
    a = get_float("Acceleration (m/s²): ")
    s = v0 * t + (a * t ** 2) / 2
    print(f"Path = {s:.2f} m")

def speed_with_acceleration():
    v0 = get_float("Initial speed (m/s): ")
    a = get_float("Acceleration (m/s²): ")
    t = get_positive_float("Time (s): ")
    print(f"Final speed = {v0 + a * t:.2f} m/s")

def menu():
    while True:
        print("\n--- KINEMATICS ---")
        print("1. Speed (v = S/t)")
        print("2. Acceleration (a = (v - v₀)/t)")
        print("3. Path with acceleration (s = v₀t + at²/2)")
        print("4. Speed with acceleration (v = v₀ + at)")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1": speed()
        elif choice == "2": acceleration()
        elif choice == "3": path_with_acceleration()
        elif choice == "4": speed_with_acceleration()
        elif choice == "0": return
        else: print("Invalid input!")