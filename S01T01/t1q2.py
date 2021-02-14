def area(r):
    return 3.14 * r**2
def perimetro(r):
    return 3.14 * 2 * r

raio = int(input("\nDigite o raio do círculo: "))
print("\nA área do círuculo é: %.2f" % area(raio))
print("\nO perímetro do círculo é %.2f: " % perimetro(raio))
