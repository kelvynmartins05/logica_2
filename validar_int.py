valor = input("Digite um número inteiro: ").strip()

if valor == "":
    print("Dado inválido")
else:
    try:
        numero = int(valor)
        print(f"Você digitou o inteiro: {numero}")
    except ValueError:
        print("Dado inválido (não é um número inteiro)")
