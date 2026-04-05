velocidade = float(input("Digite a velocidade em Km/h: "))
limite = 80

if velocidade > limite:
    excesso = velocidade - limite
    valor_multa = excesso * 50
    print(f"Limite = {limite}Km/h")
    print(f"Excedeu {excesso:.0f}Km/h")
    print(f"multa = {excesso:.0f}Km/h * R$ 50,00")
    print(f"Valor da multa: R$ {valor_multa:.2f}")
else:
    print("Velocidade dentro do limite permitido.")
