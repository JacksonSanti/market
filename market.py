from typing import List, Dict
from time import sleep

from models.product import Product
from utils.helper import format_float_to_str_coin

products: List[Product] = []
carrinho: List[Dict[Product, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print('================================')
    print('===========Bem Vindo============')
    print('============Mercado=============')
    print('================================')

    print('')
    print('Selecione uma opção abaixo: ')
    print('')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')
    print('================================')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_product()
    elif opcao == 2:
        listar_product()
    elif opcao == 3:
        comprar_product()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre')
        sleep(1)
        exit(0)
    else:
        print('Opção invalida!')
        menu()

def cadastrar_product() -> None:
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preco do produto: '))


    product: Product = Product(nome, preco)

    products.append(product)

    print(f'O produto {product.nome} foi adcionado com o preco de {format_float_to_str_coin(product.preco)}')
    sleep(1)
    menu()

def listar_product() -> None:
    if len(products) > 0:
        print('Listagem de produto')
        print('===================')

        for product in products:
            print(product)
            print('===================')
            sleep(1)
    else:
        print('Ainda não existe produtos cadastrado')
    sleep(1)
    menu()

def comprar_product() -> None:
    if (len(products)) > 0:
        print('Informe o codigo do produto que deseja adicionar ao carrinho: ')
        print('==============================================================')
        print('================== Produtos Disponiveis ======================')
        for product in products:
            print(product)
            print('==============================================================')
            sleep(1)
        codigo: int = int(input())
        product: Product = pega_product_por_codigo(codigo)

        if product:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: item = item.get(product)
                    if quant:
                        item[product] = quant + 1
                        print(f'O produto {product.nome} agora possui {quant + 1} unidades no carrignho')
                        tem_no_carrinho = True
                        sleep(1)
                        menu()
                if not tem_no_carrinho:
                    prod = {product: 1}
                    carrinho.append(prod)
                    print(f'O produto {product.nome} foi adcionado ao carrinho.')
                    sleep(1)
                    menu()
            else:
                item = {product: 1}
                carrinho.append(item)
                print(f'O produto {product.nome} foi adcionado ao carrinho')
                sleep(1)
                menu()
        else:
            print(f'O produto com codigo {codigo} não foi encontrado')
            sleep(1)
            menu()
    else:
        print('Ainda não existem productos para vender.')
    sleep(1)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos do carrinho')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('=======================')
                sleep(1)

    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(1)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {1}')
                valor_total += dados[0].preco * dados[1]
                print('=============================')
                sleep(1)
        print(f'Sua fatura é de {format_float_to_str_coin(valor_total)}')
        print('Volte sempre')
        carrinho.clear()
        sleep(2)
        menu()
    else:
        print('Ainda não ha produtos no carrinho')
    sleep(1)
    menu()

def pega_product_por_codigo(codigo: int) -> None:
    p: Product = None

    for product in products:
        if product.codigo == codigo:
            p = product
    return p



if __name__ == '__main__':
    main()