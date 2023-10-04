import textwrap
from menu import menu
from depositar import depositar
from saque import sacar
from exbibir_extrato import exibir_extrato
from exibir_saldo import exibir_saldo
from criar_usuarios import criar_usuario
from criar_conta import criar_conta


def lista_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t {conta['agencia']}
            C/C:\t\t {conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}
"""
        print("*" * 100)
        print(textwrap.dedent(linha))

def main(): #Função Menu principal
    LIMITE_SAQUE = 2
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = " "
    numeros_saque = 0
    usuarios = []
    contas = []

    while True:
        
        opcao = menu()

        if opcao == 1:
            valor = float(input("Informe o valor do saque: R$ "))
            saldo , extrato, numeros_saque, limite = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numeros_saque,
                limite_saque=LIMITE_SAQUE,
            )
            
        elif opcao == 2:
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato =  depositar(valor=valor, saldo=saldo, extrato=extrato)

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            exibir_saldo(saldo=saldo)
        
        elif opcao == 5:
            criar_usuario(usuarios)
        
        elif opcao == 6:
            numeros_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numeros_conta, usuarios)

            if conta:
                contas.append(conta)
            
        elif opcao == 7:
            lista_contas(contas)

        elif opcao == 8:
            break
main()