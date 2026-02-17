def ask_filters():
    state = input("Ingrese el departamento: ")

    while True:
        dates_amount = input("Ingrese la cantidad de datos: ")

        if dates_amount.isdigit():
            dates_amount = int(dates_amount)
            break

        print("Debe ingresar un numero valido.\n")

    return {
        "state" : state.upper(),
        "dates_amount" : dates_amount
    }