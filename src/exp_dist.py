import math
import matplotlib.pyplot as plt
import numpy as np

def calcular_probabilidad(lam, x):
    return 1 - math.exp(-lam * x)

def generar_grafico(lam):
    x = np.linspace(0, 10, 500) 
    y = lam * np.exp(-lam * x) 
    
    plt.plot(x, y, label=f"λ = {lam}")
    plt.title("Distribución Exponencial (PDF)")
    plt.xlabel("X")
    plt.ylabel("f(X)")
    plt.legend()
    plt.grid()
    plt.show()

def mostrar_menu():
    print("\n*** Menú de Distribución Exponencial ***")
    print("1. Calcular probabilidad P(X ≤ x)")
    print("2. Graficar la función de densidad de probabilidad")
    print("3. Calcular media y varianza")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                lam = float(input("Ingrese el valor de λ (tasa de variación): "))
                x = float(input("Ingrese el valor de x: "))
                probabilidad = calcular_probabilidad(lam, x)
                print(f"La probabilidad acumulada P(X ≤ {x}) es: {probabilidad:.4f}")
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")
        
        elif opcion == "2":
            try:
                lam = float(input("Ingrese el valor de λ (tasa de variación): "))
                generar_grafico(lam)
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para λ.")
        
        elif opcion == "3":
            try:
                lam = float(input("Ingrese el valor de λ (tasa de variación): "))
                media = 1 / lam
                varianza = 1 / (lam ** 2)
                print(f"La media de la distribución es: {media:.4f}")
                print(f"La varianza de la distribución es: {varianza:.4f}")
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para λ.")
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()