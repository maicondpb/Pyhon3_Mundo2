n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
if média < 5:
    print('Sua média é {:.1f} e você está REPROVADO!'.format(média))
elif média >= 5 and média <= 6.9:
    print('Sua média é {:.1f} e você ficou em RECUPERAÇÃO!'.format(média))
elif média >= 7:
    print('Sua média é {:.1f} e você foi APROVADO!'.format(média))
