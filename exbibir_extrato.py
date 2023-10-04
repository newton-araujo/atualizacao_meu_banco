def exibir_extrato(saldo, extrato): # Funçao para exibir extrato.
    print("EXTRATO".center(30, "="))
    print("Não foram realizadas movimentações" if not extrato in extrato else extrato)
    print(f"Saldo: R${saldo:.2f}")
    print("".center(30,"="))