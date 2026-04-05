texto = input("Digite um texto: ").strip() # O .strip() remove espaços vazios nas pontas

if texto == "":
    print("Dado inválido")
else:
    print(f"Você digitou: {texto}")
