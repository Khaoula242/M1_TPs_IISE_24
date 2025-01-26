from src.math_operations import add, subtract, multiply, divide
from src.string_operations import concatenate, to_uppercase
"""
Point d'entrée principal du programme.
Affiche les résultats des opérations mathématiques et sur les chaînes.
"""
def main():
    print("Addition: ", add(10, 5))
    print("Subtraction: ", subtract(10, 5))
    print("Multiplication: ", multiply(10, 5))
    print("Division: ", divide(10, 5))

    print("Concatenation: ", concatenate("Hello", " World"))
    print("Uppercase: ", to_uppercase("hello"))

if __name__ == "__main__":
    main()
