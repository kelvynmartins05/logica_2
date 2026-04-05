litros = float(input("Digite o número de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A - Álcool / G - Gasolina): ").strip().upper()

preco_alcool = 2.89
preco_gasolina = 4.95

if tipo == 'A':
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor_pago = litros * (preco_alcool - (preco_alcool * desconto))
    print(f"Valor a ser pago: R$ {valor_pago:.2f}")

elif tipo == 'G':
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor_pago = litros * (preco_gasolina - (preco_gasolina * desconto))
    print(f"Valor a ser pago: R$ {valor_pago:.2f}")

else:
    print("Tipo de combustível inválido!")
