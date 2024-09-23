batimentos = float(input('Digite seu batimento:'))
idade = int(input('Digite sua idade:'))

if idade <= 2 and 120 <= batimentos <= 140 :
    print('Seu batimento esta dentro da faixa adequada')
elif 8 <= idade <= 18 and 80 <= batimentos <= 100:
    print ('Seu batimento esta dentro da faixa adequada')
elif idade >= 18 and 70 <= batimentos <= 80: 
    print('Seu batimento esta dentro da faixa adequada')
elif idade > 60 and 50 <= batimentos <= 60:
    print('Seu batimento esta dentro da faixa adequada')
else: 
    print('Vá para o hospital')















