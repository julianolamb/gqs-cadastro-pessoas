# Sistema de Cadastro de Pessoas - versao 2
# novos requisitos: menu, consulta, alteracao e listagem

def exibir_menu():
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    return int(input("Escolha uma opcao: "))
 
def cadastrar_pessoa(nomes, idades, emails):
    nome = input("Informe o nome: ")
    nomes.append(nome)
    idade = int(input("Informe a idade: "))
    idades.append(idade)
    email = input("Informe o email: ")
    emails.append(email)
    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def exibir_pessoa(nomes, idades, emails, pos):
    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])
    if idades[pos] >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")
 
def buscar_pessoa(nomes, nome_procurado):
    pos = 0
    while pos < len(nomes):
        if nomes[pos] == nome_procurado:
            return pos
        pos = pos + 1
    return -1

def consultar_pessoa(nomes, idades, emails):
    procurado = input("Nome para consultar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        exibir_pessoa(nomes, idades, emails, pos)


nomes = []
idades = []
emails = []
 
qtd = 0
op = 0
 
while op != 5:
    #print("=========================")
    #print(" CADASTRO DE PESSOAS")
    #print("=========================")
    #print("1 - Cadastrar pessoa")
    #print("2 - Consultar pessoa")
    #print("3 - Alterar pessoa")
    #print("4 - Listar pessoas")
    #print("5 - Sair")
    #op = int(input("Escolha uma opcao: "))

    op = exibir_menu()
 
    if op == 1:
        cadastrar_pessoa(nomes, idades, emails)
    elif op == 2:
        consultar_pessoa(nomes, idades, emails)
  
    elif op == 3:
        pos = 0
        achou = 0
        nome_busca = input("Informe um nome para busca: ")
        while pos < len(nomes):
            if (nomes[pos] == nome_busca):
                nomes[pos] = input("Informe o novo nome: ")
                idades[pos] = input("Informe a nova idade: ")
                emails[pos] = input("Informe o novo email: ")
                achou = 1
            pos = pos + 1
        if achou == 0:
            print("Usuario não encontrado!")        
    elif op == 4:
        pos = 0
        while pos < len(nomes):
            print("Nome: " + nomes[pos])
            print("Idade: " + str(idades[pos]))
            print("Email: " + emails[pos])
            pos = pos + 1
    elif op == 5:
        print("Saindo...")
 
    else:
        print("Opcao invalida")
 
print("Fim do programa")
