def celsius(a):
    C = ((F - 32) / 9) * 5
    return C

F = float(input("Digite uma temperatura em Fahrenheit: "))
resultado = celsius(F)
print(f'{F} graus em Fahrenheit é equivalente a {resultado:.2f} graus em celsius')




