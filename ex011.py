'''
Exercício Python 11: Faça um programa que leia a largura
e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''


largura = float(input('Qual a largura da sua parede? '))
altura = float(input('Qual a altura da sua parede? '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m²'.format(largura, altura, area))
tinta = area / 2
print(f'Para pintar essa parede, vc precisará de {tinta} Litros de tinta. ')

