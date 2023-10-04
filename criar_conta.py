from filtrar_usuarios import filtrar_usuarios

def criar_conta(agencia, conta, usuários):
    cpf = input("Informe seu cpf: ")
    usuário = filtrar_usuarios(cpf, usuários)

    if usuário:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta":conta, "usuario":usuário}
    
    print("Usuário não encontrado!")