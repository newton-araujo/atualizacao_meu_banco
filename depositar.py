def depositar(valor, saldo, extrato): #Função depósito.
    if valor > 0:
        saldo += valor
        extrato += f"Deposito ---- R$ {valor:.2f}\n"
        print("Depósito realizado!")
    elif valor < 0:
        print("Valor incerreto, tente novamente")

    return saldo, extrato