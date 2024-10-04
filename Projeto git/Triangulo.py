def fn_tri_verifica():
    # pedindo o valor dos lados
    lado1 = int(input("Digite um número inteiro entre 1 e 10 para o lado1: "))
    lado2 = int(input("Digite um número inteiro entre 1 e 10 para o lado2: "))
    lado3 = int(input("Digite um número inteiro entre 1 e 10 para o lado3: "))
    # forçando o lado1 para ser o lado maior
    if lado1 < lado2:
        ladoaux = lado1
        lado1 = lado2
        lado2 = ladoaux
    if lado1 < lado3:
        ladoaux = lado1
        lado1 = lado3
        lado3 = ladoaux
    # se lado maior
    if lado1 < lado2 + lado3:
        print("Os lados formam um triangulo")
        fn_tri_tipo(lado1, lado2, lado3)
        return
    print("Os lados não formam um triangulo")
    return

def fn_tri_tipo(lado1a, lado2a, lado3a):
    if lado1a == lado2a == lado3a:
        print("Equilátero")
    else:
        if lado1a != lado2a != lado3a:
            print("Escaleno")
        else: print("Isosceles")
    return
