def filtrar_usuarios(cpf, usuarios): #Função para verificar usuários cadastrados
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None