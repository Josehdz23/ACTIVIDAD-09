clientes = {}
def menu():
    print("\n1. Agregar Clientes\n2. Mostrar clientes y destinos visitados\n3. Salir")

def agregarClientes():
    try:
            while True:
                cantidad = int(input("\nIngrese la cantidad de clientes que agregará: "))
                for i in range(cantidad):
                    print(f"CLIENTE #{i+1}")
                    while True:
                        try:
                            codigo = int(input("Ingrese el codigo del cliente: "))
                            if codigo > 0:
                                if codigo in clientes:
                                    print(f"Este codigo ya existe en la lista {codigo}")
                                else:
                                    break
                            else:
                                print("El codigo del cliente no es valido\n")
                        except Exception as ex:
                            print(f"Ocurrió un error: {ex}\n")
                    while True:
                        nombre = input("Ingrese el nombre del cliente: ")
                        if nombre or nombre.isspace():
                            break
                        else:
                            print(f"El nombre del cliente no es valido!\n")
                    clientes[codigo] = {
                        "nombre": nombre,
                        "destinos": {}
                    }
                    while True:
                        try:
                            noDestinos = int(input("Ingrese cuantos destinos visitará el cliente (1 - 5): "))
                            if noDestinos > 0 and noDestinos <= 5:
                                for j in range(noDestinos):
                                    destino = input(f"Destino #{j+1}: ")
                                    clientes[codigo]["destinos"][destino] = True
                                break
                            else:
                                print("Número de destinos no válido, reintente")
                        except Exception as ex:
                            print(f"Ocurrió un error: {ex}")
                break
    except Exception as ex:
        print(f"Ocurrió un error: {ex}")

def mostrarClientes():
    if clientes:
        for clave, dato in clientes.items():
            h = 0
            print(f"\nCodigo: {clave}, Nombre: {dato['nombre']}")
            for dato2 in dato["destinos"]:
                print(f"Destino {h + 1}: {dato2}")
                h = h + 1
        destinosTotales = [dato["destinos"] for dato in clientes.values()]
        total = contarDestinos(destinosTotales)
        print(f"\nTotal de destinos registrados: {total}")

        listaClientes = list(clientes.values())
        listaCodigos = list(clientes.keys())

        mayor = masDestinos(listaClientes, listaCodigos)
        if mayor:
            print(f"Cliente con más destinos: {mayor[1]} (Código: {mayor[0]}) con {mayor[2]} destinos")
    else:
        print("\nNo hay clientes en la lista")

def contarDestinos(lista, cont = 0):
    if cont == len(lista):
        return 0
    return len(lista[cont]) + contarDestinos(lista, cont + 1)

def masDestinos(lista, codigo, cont = 0, mayor = None):
    if cont == len(lista):
        return mayor

    destinos_actual = len(lista[cont]["destinos"])
    if mayor is None or destinos_actual > mayor[2]:
        mejor = (codigo[cont], lista[cont]["nombre"], destinos_actual)

    return masDestinos(lista, codigo, cont + 1, mayor)


def main():
    while True:
        menu()
        try:
            opcion = int(input("Escoga una opción: "))
            match opcion:
                case 1:
                    agregarClientes()
                case 2:
                    mostrarClientes()
                case 3:
                    print("Saliendo...")
                    break
                case _:
                    print("Esa opción no existe! Reintente")
        except Exception as ex:
            print(f"Ocurrió un error: {ex}")

main()