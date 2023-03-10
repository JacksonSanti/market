from utils.helper import format_float_to_str_coin


class Product:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo: int = Product.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Product.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco

    def __str__(self) -> str:
        return f'Codigo: {self.codigo} \nNome: {self.nome} \nPreco: {format_float_to_str_coin(self.preco)} \n'
