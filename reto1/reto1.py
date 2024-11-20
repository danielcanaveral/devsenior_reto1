from datetime import datetime
import statistics

class Experimento:
    def __init__(self, nombre, fechaRealizacion, tipo, resultados):
        self.nombre = nombre
        self.fechaRealizacion = fechaRealizacion
        self.tipo = tipo
        self.resultados = resultados


def agregarExperimento(listaExperimentos):
    nombre = input("Ingrese el nombre del experimento: ")
    fechaRealizacion_str = input("Ingrese la fecha de realización del experimento (dd/mm/aaaa): ")
    try:
        fechaRealizacion = datetime.strptime(fechaRealizacion_str, "%d/%m/%Y")
    except ValueError:
        print("Fecha no válida. Debe ser dd/mm/aaaa.")
        return

    tipo = input("Ingrese el tipo de experimento (Físico, Químico, Biológico, etc.): ")
    resultados_str = input("Ingrese los resultados obtenidos separados por comas (ejemplo: 12.3,15.8,9.2): ")
    try:
        resultados = list(map(float, resultados_str.split(",")))
        if not resultados:
            raise ValueError
    except ValueError:
        print("Resultados no válidos. Debe ingresar números separados por comas.")
        return

    experimento = Experimento(nombre, fechaRealizacion, tipo, resultados)
    listaExperimentos.append(experimento)
    print("Experimento agregado exitosamente.")


def visualizarExperimentos(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados.")
        return
    
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"\nExperimento {i}:")
        print(f"Nombre: {experimento.nombre}")
        print(f"Fecha de realización: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}")
        print(f"Tipo: {experimento.tipo}")
        print(f"Resultados: {experimento.resultados}")


def analizarResultados(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados.")
        return

    for experimento in listaExperimentos:
        promedio = statistics.mean(experimento.resultados)
        maximo = max(experimento.resultados)
        minimo = min(experimento.resultados)

        print(f"\nAnálisis de {experimento.nombre}")
        print(f"Promedio de resultados: {promedio:.2f}")
        print(f"Máximo resultado: {maximo}")
        print(f"Mínimo resultado: {minimo}")


def generarInforme(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos registrados.")
        return

    with open("informe_experimentos.txt", "w") as archivo:
        for experimento in listaExperimentos:
            archivo.write(f"Nombre: {experimento.nombre}\n")
            archivo.write(f"Fecha de realización: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}\n")
            archivo.write(f"Tipo: {experimento.tipo}\n")
            archivo.write(f"Resultados: {experimento.resultados}\n")
            promedio = statistics.mean(experimento.resultados)
            maximo = max(experimento.resultados)
            minimo = min(experimento.resultados)
            archivo.write(f"Promedio de resultados: {promedio:.2f}\n")
            archivo.write(f"Máximo resultado: {maximo}\n")
            archivo.write(f"Mínimo resultado: {minimo}\n")
            archivo.write("\n")
    print("Informe generado como informe_experimentos.txt.")


def menu():
    listaExperimentos = []

    while True:
        print("\n MENU DE OPCIONES")
        print("1. Agregar experimento")
        print("2. Visualizar experimentos")
        print("3. Analizar resultados experimentales")
        print("4. Generar informe")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregarExperimento(listaExperimentos)
        elif opcion == "2":
            visualizarExperimentos(listaExperimentos)
        elif opcion == "3":
            analizarResultados(listaExperimentos)
        elif opcion == "4":
            generarInforme(listaExperimentos)
        elif opcion == "5":
            print("Gracias por usar el sistema de gestión de experimentos.")
            break
        else:
            print("Opción no válida. Ingrese un número entre 1 y 5.")


if __name__ == "__main__":
    menu()