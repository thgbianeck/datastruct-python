# data_structures/array/array.py

class Array:
    """
    Classe que representa uma estrutura de dados do tipo Array.
    Permite operações básicas como inserção, remoção e busca de elementos.
    """

    def __init__(self):
        """
        Inicializa um array vazio.
        """
        self._items = []

    def insert(self, item):
        """
        Insere um item no final do array.

        :param item: O item a ser inserido.
        """
        self._items.append(item)

    def remove(self, item):
        """
        Remove a primeira ocorrência de um item no array.
        Se o item não estiver presente, não faz nada.

        :param item: O item a ser removido.
        """
        try:
            self._items.remove(item)
        except ValueError:
            # O item não estava no array, então não há nada a fazer.
            pass

    def search(self, item):
        """
        Busca por um item no array.

        :param item: O item a ser buscado.
        :return: True se o item estiver presente, False caso contrário.
        """
        return item in self._items

    def get_items(self):
        """
        Retorna todos os itens presentes no array.

        :return: Uma lista com todos os itens do array.
        """
        return self._items
