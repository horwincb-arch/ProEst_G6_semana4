import aritmetica as arit

def menu():
    print("Bienvenido a mi calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")
    op = int(input("Digite el # de la ecuacion que desea usar: "))

def showAdd(num1, num2):
    print(f"La suma de {num1} + {num2} es: {arit.add(num1, num2)}")
def showSub(num1, num2):
    print(f"La diferencia de {num1} - {num2} es: {arit.sub(num1, num2)}")
def showMult(num1, num2):
    print(f"El producto de {num1} * {num2} es: {arit.mult(num1, num2)}")
def showDiv(num1, num2):
    print(f"La division de {num1} / {num2} es: {arit.div(num1, num2)}")

def readValues():
    num1 = float(input("Digite el primer numero: "))
    num2 = float(input("Digite el segundo numero: "))
    return num1, num2
def chooseOP(op):
    if op == 1:
        num1, num2 = readValues()
        showAdd(num1, num2)
    elif op == 2:
        num1, num2 = readValues()
        showSub(num1, num2)
    elif op == 3:
        num1, num2 = readValues()
        showMult(num1, num2)
    elif op == 4:
        num1, num2 = readValues()
        showMult(num1, num2)
    elif op == 0:
        print("Adios.")

    else:
        print("Opcion no valida.")

def main():
    while True:
        op = menu()
        chooseOP(op)
        if op == 0: break
main()
    