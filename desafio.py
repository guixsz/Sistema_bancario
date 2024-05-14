menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=>  '''

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

    

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))


        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
            print(extrato + f"Seu saldo atual: {saldo}")
    
    
        else: 
            print("Você não pode depositar um valor negativo")      

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if  valor > saldo:
            print("Você não tem saldo suficiente")
        
        elif valor > LIMITE:
            print("O valor de saque excedeu o limite")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Excedeu o limite de saques por dia")
        
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor: .2f}\n"
            print(extrato + f"Seu saldo atual: {saldo}")


    elif opcao == "e":

        print("\n======================= EXTRATO ========================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("==========================================================")
                
        
    elif opcao == "q":
        break;