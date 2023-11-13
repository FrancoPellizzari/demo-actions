def dividir(a, b):
 if b == 0:
        raise ValueError("No se puede dividir por cero")
 return a / b



if __name__ == "__main__":
    try:
        resultado = dividir(5, 3)
        print(resultado)
        
        # Intentando dividir por cero
        resultado_division_cero = dividir(5, 0)
        print(resultado_division_cero)

    except ValueError as e:
        print(f"Error: {e}")