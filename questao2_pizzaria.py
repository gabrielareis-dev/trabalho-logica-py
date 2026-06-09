# Mensagem de boas vindas e cardápio da pizzaria
print("Bem-vindo a Pizzaria da Gabriela Loura")
print("------------ CARDÁPIO ------------")
print("Tamanho P - Pizza Salgada (PS) = R$30 | Pizza Doce (PD) = R$34")
print("Tamanho M - Pizza Salgada (PS) = R$45 | Pizza Doce (PD) = R$48")
print("Tamanho G - Pizza Salgada (PS) = R$60 | Pizza Doce (PD) = R$66")
print("----------------------------------")

# Variável para guardar o total do pedido
Total = 0

# Loop para fazer os pedidos
while True:  

    # Valida sabor
    while True:
        sabor = input("Digite o sabor da pizza (PS para salgada ou PD para doce): ").upper()
        if sabor == "PS" or sabor == "PD":
            break
        else:
            print("Sabor inválido. Escolha PS ou PD.")
            continue

    # Loop para validar os tamanhos de pizza
    while True:
        tamanho = input("Digite o tamanho da pizza (P, M ou G): ").upper()
        if tamanho == "P" or tamanho == "M" or tamanho == "G":
            break
        else:
            print("Tamanho inválido. Escolha P, M ou G.")
            continue

    # Calcula o valor da pizza
    if sabor == "PS":
        if tamanho == "P":
            valor = 30
        elif tamanho == "M":
            valor = 45
        else:
            valor = 60
    else:  
        if tamanho == "P":
            valor = 34
        elif tamanho == "M":
            valor = 48
        else:
            valor = 66

    Total += valor

    # Pergunta se quer continuar fazendo pedidos
    continuar = input("Deseja mais alguma coisa? (S/N): ").upper()
    if continuar != "S":
        break

print(f"O total do pedido foi R$ {Total:.2f}")
# Mostra o total do pedido

