from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()

def menu() -> None:
    print('============================')
    print('============ATM=============')
    print('===========BANCO============')
    print('============================')

    print('Selecione uma opção no menu:')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - efetuar deposito')
    print('4 - Efetuar transferencia')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Obrigado por usar o Banco!')
        sleep(2)
        exit()
    else:
        print('Opção inválida!')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente')
    nome: str = input('Nome: ')
    email: str = input('Email: ')
    cpf: str = input('CPF: ')
    data_nascimento: str = input('Data de nascimento (dd/mm/aaaa): ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da conta:')
    print('---------------------------')
    print(conta)
    sleep(3)
    menu()

def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o numero da sua conta: '))
          
        conta: Conta = buscar_contar_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)

        else:
            print(f'Não foi encontrada a conta de numero {numero}')


    else:
        print('Ainda nao existem contas cadastradas')

    sleep(2)
    menu()

def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o numero da sua conta: '))

        conta: Conta = buscar_contar_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do deposito: '))
            conta.depositar(valor)

        else:
            print(f'Não foi encontrada a conta de numero {numero}')
    else:
        print('Ainda nao existem contas cadastradas')
    
    sleep(2)
    menu()

def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o numero de sua conta: '))
        conta_o: Conta = buscar_contar_por_numero(numero_o)

        if conta_o: 
            numero_d: int = int(input('Informe o numero da conta do destinatario: '))
            conta_d: Conta = buscar_contar_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferencia'))
                conta_o.transferir(conta_d, valor)

            else:
                print(f'A conta do destinatario de numero {numero_d} não foi encontrada')

        else:
            print(f'A sua conta de numero {numero_o} não foi encontrada')

    else:
        print('Ainda nao existem contas cadastradas')
    
    sleep(2)
    menu()

def listar_contas() -> None:
    if len(contas) > 0:
        for conta in contas:
            print(conta)
            print('---------------------')
            sleep(1)

    else:
        print('Ainda nao existem contas cadastradas')
    
    sleep(2)
    menu()

def buscar_contar_por_numero(numero:int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
       for conta in contas:
           if conta.numero == numero:
                c = conta 

    return c

if __name__ == '__main__':
    main()