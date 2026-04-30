from collections import Counter

usuario_correto = "admin"
senha_correta = 1234
tentativas = 3
logado = False


listagem_produtos = {
    "Código": [1],
    "Nome": ["Pamonha"],
    "Preço": [12.50],
    "Estoque": [20]
}

historico_produto = []
historico_qtd = []
historico_valor = []

while tentativas > 0:
    print(f"\nTentativas restantes: {tentativas}")
    usuario_input = input("Usuário: ")

    try:
        senha_input = int(input("Senha: "))

        if usuario_input == usuario_correto and senha_input == senha_correta:
            print("Login realizado com sucesso!")
            logado = True
            break
        else:
            print("Usuário ou senha incorretos.")
            tentativas -= 1
    except ValueError:
        print("Erro: A senha deve ser numérica!")
        tentativas -= 1

if not logado:
    print("SISTEMA BLOQUEADO!")
    exit()


while True:
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Atualizar estoque")
    print("4. Realizar venda")
    print("5. Relatórios")
    print("6. Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida! Digite um número.")
        continue

    if opcao == 1:
        try:
            codigo = int(input("Código (int): "))
            if codigo in listagem_produtos["Código"]:
                print("Erro: Código já cadastrado!")
                continue

            nome = input("Nome: ")
            preco = float(input("Preço: "))
            qtd = int(input("Quantidade inicial: "))

            if preco < 0 or qtd < 0 or codigo < 0:
                print("Erro: Não são permitidos valores negativos!")
                continue

            listagem_produtos["Código"].append(codigo)
            listagem_produtos["Nome"].append(nome)
            listagem_produtos["Preço"].append(preco)
            listagem_produtos["Estoque"].append(qtd)
            print("Produto cadastrado!")
        except ValueError:
            print("Erro: Entrada inválida para números.")

    elif opcao == 2:
        if not listagem_produtos["Código"]:
            print("Nenhum produto cadastrado.")
        else:
            print("\nCódigo | Nome | Preço | Estoque")
            for i in range(len(listagem_produtos["Código"])):
                print(
                    f"{listagem_produtos['Código'][i]} | {listagem_produtos['Nome'][i]} | R${listagem_produtos['Preço'][i]:.2f} | {listagem_produtos['Estoque'][i]}")

    elif opcao == 3:
        try:
            cod_busca = int(input("Digite o código do produto: "))
            if cod_busca not in listagem_produtos["Código"]:
                print("Produto não encontrado!")
                continue

            idx = listagem_produtos["Código"].index(cod_busca)
            print("1. Adicionar estoque | 2. Remover estoque")
            sub_op = int(input("Opção: "))
            v_alt = int(input("Quantidade: "))

            if v_alt < 0:
                print("Digite um valor positivo para a operação.")
                continue

            if sub_op == 1:
                listagem_produtos["Estoque"][idx] += v_alt
            elif sub_op == 2:
                if listagem_produtos["Estoque"][idx] - v_alt < 0:
                    print("Erro: Estoque não pode ficar negativo!")
                else:
                    listagem_produtos["Estoque"][idx] -= v_alt
            else:
                print("Opção inválida.")
        except ValueError:
            print("Erro: Digite apenas números.")

    elif opcao == 4:
        try:
            cod_venda = int(input("Código do produto: "))
            if cod_venda not in listagem_produtos["Código"]:
                print("Produto inexistente!")
                continue

            idx = listagem_produtos["Código"].index(cod_venda)
            qtd_venda = int(input("Quantidade: "))

            if qtd_venda <= 0:
                print("Quantidade deve ser maior que zero.")
                continue

            if qtd_venda > listagem_produtos["Estoque"][idx]:
                print("Estoque insuficiente!")
                continue

            valor_venda = qtd_venda * listagem_produtos["Preço"][idx]
            listagem_produtos["Estoque"][idx] -= qtd_venda


            historico_produto.append(listagem_produtos["Nome"][idx])
            historico_qtd.append(qtd_venda)
            historico_valor.append(valor_venda)
            print(f"Venda realizada! Total: R${valor_venda:.2f}")
        except ValueError:
            print("Erro: Entrada inválida.")

    elif opcao == 5:
        print("\n1. Total vendido | 2. Mais vendido | 3. Maior estoque | 4. Listar vendas")
        try:
            rel_op = int(input("Opção: "))
            if rel_op == 1:
                print(f"Total arrecadado: R${sum(historico_valor):.2f}")
            elif rel_op == 2:
                if not historico_produto:
                    print("Nenhuma venda registrada.")
                else:
                    mais_vendido = Counter(historico_produto).most_common(1)[0][0]
                    print(f"Produto mais vendido: {mais_vendido}")
            elif rel_op == 3:
                maior_est = max(listagem_produtos["Estoque"])
                idx_est = listagem_produtos["Estoque"].index(maior_est)
                print(f"Maior estoque: {listagem_produtos['Nome'][idx_est]} ({maior_est} un)")
            elif rel_op == 4:
                print("Histórico de Vendas:", historico_produto)
        except ValueError:
            print("Erro na seleção.")


    elif opcao == 6:
        print("\n--- RESUMO DO SISTEMA ---")
        print(f"Produtos cadastrados: {len(listagem_produtos['Código'])}")
        print(f"Vendas realizadas: {len(historico_produto)}")
        print(f"Valor total vendido: R${sum(historico_valor):.2f}")
        break
    else:
        print("Opção inexistente.")