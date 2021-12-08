total = 1
totalsim = 0
totalnao = 0
homensnao = 0
mulhersim = 0
percentual = 0
while True:
    idade = int(input('Qual a sua idade?: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper()
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Voce gostou do novo produto?: [S/N]')).upper()
    if perg == 'S':
        totalsim += 1
    if perg == 'N':
        totalnao += 1
    if sexo == 'M' and perg == 'N':
        homensnao += 1
    if sexo == 'F' and perg == 'S':
        mulhersim += 1
    if perg =='N':
        percentual = (totalnao / total)*100
    resp = ' '
    while resp not in 'SN' :
        resp = str(input('Quer continuar?: [S/N]')).upper()
    if  resp != 'N':
        total += 1
    if resp == 'N':
        break
print('Acabou a pesquisa!')
print('====resultados===')
print('Total de entrevistado {} '.format(total))
print('A quantidade de Sim foi: {}'.format(totalsim))
print('A quantidade de Não foi: {}'.format(totalnao))
print('Mulheres que disse sim é: {}'.format(mulhersim))
print('Homens que disee não é : {}'.format(homensnao))
print('O percentual de pessoas que disseram não é: {: .2f} %'.format(percentual))
