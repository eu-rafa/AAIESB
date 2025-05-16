# Declarando as listas para armazenar os dados elegidos posteriormente
produtos = []
clientes = []
pedidos = []


# Função para exibir o menu através de chamadas e evitar repetições
def menu():
    print(f'SISTEMA COFFEE SHOPS TIA ROSA')
    print('[1] Cadastrar um Produto')
    print('[2] Cadastrar um Cliente')
    print('[3] Realizar Pedido')
    print('[4] Ver Relatório')
    print('[5] Sair')


# Função para cadastrar um produto (pensado para o uso do estabelecimento)
def cadastrar_produto():
    print('OPÇÃO 1 - CADASTRAR PRODUTO')
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    ingredientes = str(input('Ingredientes: '))
    produto = {
        'nome': nome,
        'preco': preco,
        'ingredientes': [ingrediente.strip() for ingrediente in ingredientes.split(',')]
    }
    produtos.append(produto)
    print(f'"{nome}" cadastrado com sucesso!')


# Função para cadastrar um cliente (pensado para o uso do cliente)
def cadastrar_cliente():
    print('OPÇÃO 2 - CADASTRAR CLIENTE')
    nome = str(input('Digite seu nome: '))
    telefone = str(input('Telefone para contato: '))
    email = str(input('E-mail: '))
    if '@' not in email:
        print ('E-mail inválido.')
        return
    cliente = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    clientes.append(cliente)
    print(f'"{nome}" cadastrado com sucesso!')


# Função para realizar um pedido (pensado para o uso do cliente)
def fazer_pedido():
    print('OPÇÃO 3 - FAZER PEDIDO')
    print('CLIENTES:')
    for i, cliente in enumerate(clientes):
        print(f'[{i}] {cliente["nome"]}')
    cliente_num = int(input('Selecione o número do cliente: '))
    if cliente_num < 0 or cliente_num >= len(clientes):
        print("Cliente inválido.")
        return
    cliente = clientes[cliente_num]
    sacola = []
    while True:
        print('PRODUTOS DISPONÍVEIS:')
        for i, produto in enumerate(produtos):
            print(f'[{i}] {produto["nome"]} - R${produto["preco"]:.2f}')
        produto_num = int(input('Selecione o número do produto ou digite -1 para finalizar: '))
        if produto_num == -1:
            break
        if produto_num < 0 or produto_num >= len(produtos):
            print("Produto inválido.\n")
            continue
        sacola.append(produtos[produto_num])
    if not sacola:
        print('Nenhum produto foi selecionado.')
        return
    pedido = {
        'cliente': cliente,
        'produtos': sacola,
        'total': sum(produto['preco'] for produto in sacola)
    }
    pedidos.append(pedido)
    print(f'Pedido realizado com sucesso para {cliente["nome"]}!')


# Função para analisar o relatório
def relatorio():
    print(f'RELATÓRIO')
    print('PRODUTOS:')
    for p in produtos:
        print(f'{p["nome"]} - R${p["preco"]:.2f} - Ingredientes: {", ".join(p["ingredientes"])}')
    print('PEDIDOS REALIZADOS:')
    if pedidos:
        for i, pedido in enumerate(pedidos):
            produtos_pedido = ", ".join(p['nome'] for p in pedido['produtos'])
            print(f'[{i}] Cliente: {pedido["cliente"]["nome"]} | Produtos: {produtos_pedido} | Total: R${pedido["total"]:.2f}')
    else:
        print('Nenhum pedido realizado ainda.')


# Função principal para a execução do script sem a necessidade de repetir os mesmos comandos, apenas com o uso das funções
def main():
    while True:
        menu()
        opcao = int(input('Escolha uma opção: '))
        
        match opcao:
            case 1:
                cadastrar_produto()
            case 2:
                cadastrar_cliente()
            case 3:
                fazer_pedido()
            case 4:
                relatorio()
            case 5:
                print('Coffee Shops da Tia Rosa agradece pela preferência. Volte sempre!')
                break
            case _:
                print('Opção inválida.')
if __name__ == "__main__":
    main()