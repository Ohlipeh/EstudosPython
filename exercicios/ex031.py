distancia = float(input("Qual a distância da sua viagem em km? "))
print(f"Você está prestes a começar uma viagem de {distancia:.1f} km.")
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f"E o preço da sua passagem será de R$ {preco:.2f}.")
