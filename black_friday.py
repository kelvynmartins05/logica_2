preco_total = float(input("Informe o preço total da venda: R$ "))

print("\nCondições de Pagamento:")
print("1 - À vista (em espécie) - 10% de Desconto")
print("2 - Cartão de débito - 5% de Desconto")
print("3 - Cartão de crédito - 3% de Desconto")
print("4 - PIX - 7.5% de Desconto")
codigo = input("Digite o código da condição de pagamento: ")

if codigo == '1':
    desconto = 0.10
elif codigo == '2':
    desconto = 0.05
elif codigo == '3':
    desconto = 0.03
elif codigo == '4':
    desconto = 0.075
else:
    desconto = 0
    print("Código inválido. A compra não terá desconto.")

valor_final = preco_total - (preco_total * desconto)
print(f"Valor final a ser pago: R$ {valor_final:.2f}")
