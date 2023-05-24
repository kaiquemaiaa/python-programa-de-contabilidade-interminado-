
contas_pagar = ContasPagar()
contas_receber = ContasReceber()

def cadastrar_nota_pagar():
    fornecedor = input("Digite o nome do fornecedor: ")
    cnpj = input("Digite o CNPJ: ")
    descricao = input("Digite a descrição: ")
    numero_nfe = input("Digite o número da NFe: ")
    valor = float(input("Digite o valor: "))

    contas_pagar.cadastrar_nota_fiscal(fornecedor, cnpj, descricao, numero_nfe, valor)

def pagar_nota_pagar():
    numero_nfe = input("Digite o número da NFe que deseja pagar: ")
    for nota in contas_pagar.notas_fiscais:
        if nota.numero_nfe == numero_nfe:
            nota.pagar()
            print("Nota fiscal paga com sucesso!")
            break
    else:
        print("Nenhum registro encontrado para o número da NFe informado.")

def exibir_notas_pagar():
    for nota in contas_pagar.notas_fiscais:
        nota.exibir_informacoes()
        print()

def exibir_total_pagar():
    total_pagar = contas_pagar.exibir_total_pagar()
    print("Valor total a pagar:", total_pagar)

def cadastrar_nota_receber():
    cliente = input("Digite o nome do cliente: ")
    cnpj = input("Digite o CNPJ: ")
    descricao = input("Digite a descrição: ")
    numero_nfe = input("Digite o número da NFe: ")
    valor = float(input("Digite o valor: "))

    contas_receber.cadastrar_nota_fiscal(cliente, cnpj, descricao, numero_nfe, valor)

def receber_nota_receber():
    numero_nfe = input("Digite o número da NFe que deseja receber: ")
    for nota in contas_receber.notas_fiscais:
        if nota.numero_nfe == numero_nfe:
            nota.pagar()
            print("Nota fiscal recebida com sucesso!")
            break
    else:
        print("Nenhum registro encontrado para o número da NFe informado.")

def exibir_notas_receber():
    for nota in contas_receber.notas_fiscais:
        nota.exibir_informacoes()
        print()

def exibir_total_receber():
    total_receber = contas_receber.exibir_total_receber()
    print("Valor total a receber:", total_receber)

def exibir_saldo_geral():
    total_receber = contas_receber.exibir_total_receber()
    total_pagar = contas_pagar.exibir_total_pagar()
    saldo_geral = total_receber - total_pagar
    print("Saldo geral:", saldo_geral)

while True:
    print("=== MENU ===")
    print("1. Cadastrar nota fiscal (contas a pagar)")
    print("2. Pagar nota fiscal (contas a pagar)")
    print("3. Exibir notas fiscais (contas a pagar)")
    print("4. Exibir valor total a pagar")
    print("5. Cadastrar nota fiscal (contas a receber)")
    print("6. Receber nota fiscal (contas a receber)")
    print("7. Exibir notas fiscais (contas a receber)")
    print("8. Exibir valor total a receber")
    print("9. Exibir saldo geral")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_nota_pagar()
    elif opcao == "2":
        pagar_nota_pagar()
    elif opcao == "3":
        exibir_notas_pagar()
    elif opcao == "4":
        exibir_total_pagar()
    elif opcao == "5":
        cadastrar_nota_receber()
    elif opcao == "6":
        receber_nota_receber()
    elif opcao == "7":
        exibir_notas_receber()
    elif opcao == "8":
        exibir_total_receber()
    elif opcao == "9":
        exibir_saldo_geral()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Digite novamente.")

