# tests/array/test_array.py
import pytest
from data_structures.array.array import Array

@pytest.fixture
def array():
    """
    Fixture que fornece um array vazio para os testes.
    """
    return Array()

def test_dado_um_array_vazio_quando_inserir_um_item_entao_deve_conter_o_item(array):
    """
    Testa a inserção de um item em um array vazio.
    """
    # Dado um array vazio (fornecido pela fixture)
    
    # Quando um item for inserido
    array.insert(1)
    
    # Então o array deve conter o item
    assert array.get_items() == [1]
    # E o tamanho do array deve ser 1
    assert array.size() == 1

def test_dado_um_array_com_um_item_quando_remover_o_item_entao_deve_estar_vazio(array):
    """
    Testa a remoção de um item de um array que contém um único item.
    """
    # Dado um array com um item
    array.insert(1)
    
    # Quando o item for removido
    array.remove(1)
    
    # Então o array deve estar vazio
    assert array.get_items() == []
    # E o tamanho do array deve ser 0
    assert array.size() == 0

def test_dado_um_array_com_um_item_quando_procurar_um_item_existente_entao_deve_retornar_verdadeiro(array):
    """
    Testa a busca de um item existente no array.
    """
    # Dado um array com um item
    array.insert(1)
    
    # Quando procurar um item existente
    # Então deve retornar verdadeiro
    assert array.search(1) is True

def test_dado_um_array_com_um_item_quando_procurar_um_item_inexistente_entao_deve_retornar_falso(array):
    """
    Testa a busca de um item inexistente no array.
    """
    # Dado um array com um item
    array.insert(1)
    
    # Quando procurar um item inexistente
    # Então deve retornar falso
    assert array.search(2) is False

def test_dado_um_array_quando_inserir_varios_itens_entao_tamanho_deve_refletir_o_numero_de_itens(array):
    """
    Testa se o tamanho do array reflete o número de itens após múltiplas inserções.
    """
    # Dado um array vazio
    
    # Quando inserirmos 3 itens
    array.insert(1)
    array.insert(2)
    array.insert(3)
    
    # Então o tamanho do array deve ser 3
    assert array.size() == 3

def test_dado_um_array_quando_remover_itens_entao_tamanho_deve_refletir_o_numero_de_itens_restantes(array):
    """
    Testa se o tamanho do array reflete o número de itens restantes após múltiplas remoções.
    """
    # Dado um array com 3 itens
    array.insert(1)
    array.insert(2)
    array.insert(3)
    
    # Quando removemos 2 itens
    array.remove(1)
    array.remove(2)
    
    # Então o tamanho do array deve ser 1
    assert array.size() == 1
