# Mensagem de boas vindas
print("Bem vindo a Madeireira da Lenhadora Gabriela Loura")

# Escolhe o tipo de madeira 
def escolha_tipo():
    
    while True:
        tipoMadeira = input("Escolha o tipo de madeira (PIN/PER/MOG/IPE/IMB): ").upper()
        if tipoMadeira == "PIN":
            return 150.40
        elif tipoMadeira == "PER":
            return 170.20
        elif tipoMadeira == "MOG":
            return 190.90
        elif tipoMadeira == "IPE":
            return 210.10
        elif tipoMadeira == "IMB":
            return 220.70
        else:
            print("Escolha inválida. Tente novamente.")
            
# Pergunta a quantidade de toras
def qtd_toras():
    while True:
        try:
            qtd = float(input("Digite a quantidade de toras (m³): "))
            if qtd > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras. Tente novamente.")
                continue

            if qtd < 100:
                desconto = 0
            elif qtd >= 100 and qtd < 500:
                desconto = 0.04
            elif qtd >= 500 and qtd < 1000:
                desconto = 0.09
            elif qtd >= 1000 and qtd <= 2000:
                desconto = 0.16
            else:
                print("Não aceitamos pedidos com essa quantidade de toras. Tente novamente.")
                continue

            return qtd, desconto

        except ValueError:
            print("Valor inválido. Digite um número.")
            
# Pergunta o tipo de transporte 
def transporte():
    while True:
        print("Tipo de transporte:")
        print("1 - Rodoviário (R$1000)")
        print("2 - Ferroviário (R$2000)")
        print("3 - Hidroviário (R$2500)")

        opcao = input("Escolha o transporte (1/2/3): ")

        if opcao == "1":
            return 1000
        elif opcao == "2":
            return 2000
        elif opcao == "3":
            return 2500
        else:
            print("Opção de transporte inválida.")

# Programa principal

valor_madeira = escolha_tipo()
quantidade, desconto = qtd_toras()
valor_transporte = transporte()

# Cálculo do total
total = ((valor_madeira * quantidade) * (1 - desconto)) + valor_transporte

# Resumo do pedido
print("----------------------------- RESUMO DO PEDIDO -----------------------------")
print(f"Valor da madeira por m³: R${valor_madeira:.2f}")
print(f"Quantidade: {quantidade} m³")
print(f"Desconto aplicado: {desconto*100:.0f}%")
print(f"Transporte: R${valor_transporte:.2f}")
print(f"Total a pagar: R${total:.2f}")