numero = int(input("Informe um número: "))
# u = // 1 % 10
# d = // 10 % 10
# c = // 100 % 10
# m = // 1000 % 10
n = str(numero)
print(f"Analisando o número {numero}...")
print(f"Unidade: {n[-1]}")
print(f"Dezena: {n[-2] if len(n) > 1 else 0}")
print(f"Centena: {n[-3] if len(n) > 2 else 0}")
print(f"Milhar: {n[-4] if len(n) > 3 else 0}")
