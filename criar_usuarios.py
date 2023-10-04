from filtrar_usuarios import filtrar_usuarios

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_de_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro - n° - bairro - cidade/estado): ")

    usuarios.append({"cpf":cpf,"nome":nome,"data_de_nascimento":data_de_nascimento,"endereço":endereco})

    print(usuarios)
    
    print("Cadastro realizado com sucesso!")
    

