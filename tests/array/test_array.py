# tests/array/test_array.py
import pytest
from data_structures.array.array import Array

def test_dado_um_array_vazio_quando_inserir_um_item_entao_deve_conter_o_item():
    # Dado um array vazio
    array = Array()

    # Quando um item for inserido
    array.insert(1)

    # Então o array deve conter o item
    assert array.get_items() == [1]

def test_dado_um_array_com_um_item_quando_remover_o_item_entao_deve_estar_vazio():
    # Dado um array com um item
    array = Array()
    array.insert(1)

    # Quando o item for removido
    array.remove(1)

    # Então o array deve estar vazio
    assert array.get_items() == []

def test_dado_um_array_com_um_item_quando_procurar_um_item_existente_entao_deve_retornar_verdadeiro():
    # Dado um array com um item
    array = Array()
    array.insert(1)

    # Quando procurar um item existente
    # Então deve retornar verdadeiro
    assert array.search(1) is True

def test_dado_um_array_com_um_item_quando_procurar_um_item_inexistente_entao_deve_retornar_falso():
    # Dado um array com um item
    array = Array()
    
    # Quando procurar um item inexistente
    # Então deve retornar falso
    assert array.search(2) is False
