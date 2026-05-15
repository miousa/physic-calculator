import sys
sys.path.append('..')

from utils import get_positive_float, get_nonnegative_float, get_float

G = 9.8

def force():
    m = get_positive_float("Mass (kg): ")
    a = get_float("Acceleration (m/s²): ")
    print(f"Force = {m * a:.2f} N")

def friction_force():
    mu = get_nonnegative_float("Coefficient μ: ")
    n = get_positive_float("Normal reaction (N): ")
    print(f"Friction force = {mu * n:.2f} N")

def weight():
    m = get_positive_float("Mass (kg): ")
    print(f"Weight = {m * G:.2f} N")

def elastic_force():
    k = get_positive_float("Spring stiffness (N/m): ")
    dx = get_float("Extension (m): ")
    print(f"Elastic force = {-k * dx:.2f} N")

def menu():
    while True:
        print("\n--- DYNAMICS ---")
        print("1. Force (F = m·a)")
        print("2. Friction force (F_fr = μ·N)")
        print("3. Weight (P = m·g)")
        print("4. Elastic force (F_el = -k·Δx)")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1": force()
        elif choice == "2": friction_force()
        elif choice == "3": weight()
        elif choice == "4": elastic_force()
        elif choice == "0": return
        else: print("Invalid input!")