custo = float(5.50)
tx = float(5.00)
km = []
pagar = []
valor = []

for i in range(4):
    distancia = int(input('Quantos Km tem o seu trajeto: '))
    km.append(distancia)

for i in range(4):
    valor.append(((km[i]*custo)+tx))
    print('Sua viagem vai custar: R$ {: .2f}'.format(valor[i]))
