def par_impar(a):
    if a % 2 == 0:
        return True
    else:
        return False

while True:
    try:
        num = int(input("\nDigite um número: "))
        if par_impar(num) == True:
           print("\nO número %d é par." % num)
        else:
            print("\nO número %d é ímpar." % num)
        break
    except:
        print("\nNúmero inválido. Digite novamente!")