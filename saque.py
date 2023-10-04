def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque): # Função para efetuar saque
    excedeu_saque = valor > saldo
    excedeu_limite_saque = valor > limite
    excedeu_numeros_saque = numero_saques > limite_saque
    
    if excedeu_saque:
        print("Operação falhou - Valor excedeu o seu saldo!")
    elif excedeu_limite_saque:
        print("Operação falhou - Valor de saque excedeu o limite!")
    elif excedeu_numeros_saque:
        print("Operação falho - Você excedeu o numero de saque!")
    elif valor > 0:
        saldo -= valor
        extrato += f" Saque ------- R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou - valor digitado incorreto!")

    return saldo, extrato, numero_saques, limite