usuario = "admin"
senha = 1234
tentativas = 0
vazio = False

listagem_produtos = {
    "Código": [1],
    "Nome": ["Pamonha"],
    "Preço": [12.50],
    "Estoque": [20]
}

historico_produto = []
historico_qtd = []
historico_valor = []

while tentativas < 3:
    usuario1 = str(input("Digite o usuário para entrar: "))
    senha1 = int(input("Digite a senha para entrar: "))

    if usuario1 == usuario and senha1 == senha:
        print("Login realizado com sucesso\n")
        break

    tentativas += 1

    print("Você atingiu o máximo de 3 tentativas! Tente novamente!")

while True:
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar estoque")
    print("4 - Realizar venda")
    print("5 - Relatórios")
    print("6 - Sair")
    opcao = int(input("Insira a opção: "))

    if opcao == 1:
        codigo = int(input("Insira o código do produto: "))
        nome = str(input("Insira o nome do produto: "))
        preco = float(input("Insira o preço do produto: "))
        qtd = int(input("Insira a quantidade de produtos: "))

        for code in listagem_produtos["Código"]:
            if codigo in code:
                print("Código de produto já cadastrado!")
                continue

        if qtd < 0 or preco < 0:
            print("Não podem conter valores negativos")
            continue

        listagem_produtos["Código"].append(codigo)
        listagem_produtos["Nome"].append(nome)
        listagem_produtos["Preço"].append(preco)
        listagem_produtos["Estoque"].append(qtd)

    if opcao == 2:
        for c, v in listagem_produtos.items():
            if not v:
                vazio = True
            else:
                print(c, "|", end=" ")
        print()
        for c, v in listagem_produtos.items():
            print(v, "|", end=" ")

        print()


        if vazio:
            print("Nenhum produto cadastrado!")

    if opcao == 3:
        produto = str(input("Insira o nome do produto: "))
        if produto not in listagem_produtos["Nome"]:
            print("O produto informado não existe, tente novamente!")
            continue
        else:
            estoque = int(input("Insira o estoque que você deseja adicionar ao produto: "))
            if estoque <= 0:
                print("O estoque precisa ser maior que 0!")
                continue
            if produto in listagem_produtos["Nome"]:
                indice = listagem_produtos["Nome"].index(produto)
                valor = listagem_produtos["Estoque"][indice]
                estoque_add = valor + estoque
                listagem_produtos["Estoque"].insert(indice, estoque_add)
                listagem_produtos["Nome"].pop(indice + 1)

    if opcao == 4:
        codigo = int(input("Insira o código do produto para venda: "))
        qtd = int(input("Insira a quantidade do produto que deseja vender: "))

        if codigo not in listagem_produtos["Código"]:
            print("Produto não existe! Insira um código válido!")
            continue
        indice = listagem_produtos["Código"].index(codigo)
        valor_estoque = listagem_produtos["Estoque"][indice]
        valor_preco = listagem_produtos["Preço"][indice]
        valor_produto = listagem_produtos["Nome"][indice]

        if qtd > valor_estoque:
            print("Estoque insuficiente! Insira um quantidade válida!")
            continue

        valor_estoque -= qtd
        valor_total = qtd*valor_preco

        historico_produto.append(valor_produto)
        historico_qtd.append(qtd)
        historico_valor.append(valor_total)

    if opcao == 5:
        print("Em processamento...")
    if opcao == 6:
        print("Resumo do Sistema: ")
        print("O total de produtos cadastrados no sistema é:", len(listagem_produtos["Produto"]))
        print("O total de vendas realizadas é:", len(historico_produto))
        print("O valor total vendido é:", sum(historico_produto))


















