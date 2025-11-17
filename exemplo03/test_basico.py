import pytest

@pytest.fixture
def lista_simples():
    return[1,2,3,4,5]

def test_soma(lista_simples):
    assert sum(lista_simples) == 15

def test_lenght(lista_simples):
    assert len(lista_simples) == 5

def test_elemento(lista_simples):
    assert lista_simples[0] == 1

def test_elemento1(lista_simples):
    assert lista_simples[4] == 5

def test_elemento3(lista_simples):
    assert 3 in lista_simples

def test_lista_ordenada(lista_simples):
    assert lista_simples == sorted(lista_simples)
