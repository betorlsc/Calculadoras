def calculadora(a, b, signo):
    if len([a, b, signo]) < 3:
        return "Se requieren al menos 3 parámetros."

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Los primeros dos parámetros deben ser números."

    if not isinstance(signo, str):
        return "El tercer parámetro debe ser una cadena."

    if signo == '+':
        suma = a + b
        return f"La suma de {a} + {b} es: {suma}"
    elif signo == '-':
        resta = a - b
        return f"La resta de {a} - {b} es: {resta}"
    elif signo == '*':
        multi = a * b
        return f"La multiplicación de {a} * {b} es: {multi}"
    elif signo == '/':
        division = a / b
        return f"La división de {a} / {b} es: {division}"

    return "Operación no válida."

operacion = input('Elige la operación: ')
valor1 = int(input('Ingresa el primer valor: '))
valor2 = int(input('Ingresa el segundo valor: '))
print(calculadora(valor1, valor2, operacion))