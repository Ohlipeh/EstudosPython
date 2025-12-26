real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.54
euro = real / 6.20
print(f'Com R${real:.2f} você pode comprar €{euro:.2f}')
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')