print("******************************")
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("******************************")
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("4. Sair do programa")
print("******************************")

opcao = input("Qual grandeza deseja calcular? ")

if opcao == '1':
    r = float(input("Informe o valor da Resistência (em Ώ): "))
    i = float(input("Informe o valor da Corrente (em A): "))
    u = r * i
    print(f"A Tensão encontrada é: {u} V")
elif opcao == '2':
    u = float(input("Informe o valor da Tensão (em V): "))
    i = float(input("Informe o valor da Corrente (em A): "))
    r = u / i
    print(f"A Resistência encontrada é: {r} Ώ")
elif opcao == '3':
    u = float(input("Informe o valor da Tensão (em V): "))
    r = float(input("Informe o valor da Resistência (em Ώ): "))
    i = u / r
    print(f"A Corrente encontrada é: {i} A")
elif opcao == '4':
    print("Saindo do programa...")
else:
    print("Opção inválida!")
