def menu(): #Menu visual com opções.
    print("""
    ======== Opções ========
    [1]Saque     [5]Novo Cadastro
    [2]Depósito  [6]Nova Conta   
    [3]Extrato   [7]Lista de contas   
    [4]Saldo     [8]sair      
""")
    return int(input("Opção: "))