medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
print(f'A medida de {medida}m corresponde a:')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')
print(f'{km:.3f}km')
print(f'{hm:.2f}hm')
print(f'{dam:.1f}dam')
print(f'{dm:.0f}dm')