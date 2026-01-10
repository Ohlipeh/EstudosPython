from random import randint
import time

computer = randint(0, 5)  # Faz o comoputador "pensar"
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
player = int(input("Em que número eu pensei? "))  # Jogador tenta adivinhar
print("PROCESSANDO...")
time.sleep(2)
if player == computer:
    print("Parabéns! Você me venceu!")
else:
    print(f"Ganhei! Eu pensei no número {computer} e não no {player}!")
