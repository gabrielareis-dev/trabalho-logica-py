# Mensagem de boas vindas
print("Olá, Gabriela Loura. Bem vinda ao sistema de planos de saúde")

valorBase = float(input("Digite o valor base do plano de saúde: "))
idade = int(input("Digite a idade do beneficiário: "))
# Pede os dados

if idade >= 0 and idade < 19:
    percentual = 100/100
elif idade >= 19 and idade < 29:
    percentual = 150/100
elif idade >= 29 and idade < 39:
    percentual = 225/100
elif idade >= 39 and idade < 49:
    percentual = 240/100
elif idade >= 49 and idade < 59:
    percentual = 350/100
elif idade >= 59:
    percentual = 600/100
else:
    print("Idade inválida.") 
    percentual = 0
# Vê a idade, aplica o valor e calcula o percentual

valorMensal = valorBase * percentual
# Calcula o valor final

print(f"O valor mensal do plano de saúde para um beneficiário de {idade} anos é: R$ {valorMensal:.2f}")
# Mostra o resultado