numeros = []

for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)

print("\nOs números informados foram:")
for n in numeros:
    print(n)
