salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print(f'O funcionário que ganhava R${salario:.2f}, com aumento de 15%, vai passar a ganhar R${novo:.2f}')