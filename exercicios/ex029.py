velocidade = float(input("Qual a velocidade atual do carro? "))
if velocidade > 80:  # verifica se a velocidade é maior que 80
    print("MULTADO! Você excedeu o limite de velocidade que é de 80Km/h")
    multa = (velocidade - 80) * 7  # calcula o valor da multa
    print(f"Você deve pagar uma multa de R${multa:.2f}")
print("Tenha um bom dia! Dirija com segurança!")
