numero = int(input("******************************\nInforme o número da tabuada: "))
print("******************************")

for i in range(1, 11):
    resultado = i * numero
    print(f"{i} x {numero} = {resultado}")
