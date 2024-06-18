def obtener_entrada_valida(mensaje, tipo_entrada=float):
  
  while True:
    try:
      valor = tipo_entrada(input(mensaje))
      if tipo_entrada == float and valor < 0:
        print("Error: La nota no puede ser negativa.")
      else:
        return valor
    except ValueError:
      print("Error: Entrada inválida. Ingrese un número.")

def calcular_promedio(notas):
  
  return sum(notas) / len(notas)

def main():
  
  while True:
    nombre = input("Ingrese el nombre del estudiante: ")
    matricula = input("Ingrese la matrícula del estudiante: ")

    notas = []
    for i in range(1, 5):
      nota = obtener_entrada_valida(f"Ingrese la nota {i}: ")
      notas.append(nota)

    promedio = calcular_promedio(notas)

    print("\n--- Resultados ---")
    print(f"Nombre: {nombre}")
    print(f"Matrícula: {matricula}")
    print(f"Notas: {notas}")
    print(f"Promedio: {promedio:.2f}") 

    continuar = input("¿Desea ingresar otro estudiante? (s/n): ").lower()
    if continuar != 's':
      print("Pase buenas noches!")
      break

if __name__ == "__main__":
  main()