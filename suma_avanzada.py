def suma_avanzada():
    numero_inicial = 0
    while True:
        suma_a = input("Selecciona un número para sumar o ingresa 'fin' para terminar: ")
        if suma_a.lower() == "fin":
            break
        try:
            numero = float(suma_a)
            numero_inicial += numero
        except ValueError:
            print("Ingresa un número válido.")

    print(f"El resultado de la operación es {numero_inicial}.")