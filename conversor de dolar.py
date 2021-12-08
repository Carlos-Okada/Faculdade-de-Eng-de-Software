cotacao = float(input('Cotaçao do Dolar: '))
dolar = float(input("Quantidade em Dolar: "))
conversor = dolar*cotacao
doacao = float(conversor*0.08)
print('Voce tem R${: .2f}:'.format(conversor))

if conversor>1000:
    print('O Valor para a doação é : R$ {: .2f}'.format(doacao))
else:
    print('O valor não foi suficiente para a doação')