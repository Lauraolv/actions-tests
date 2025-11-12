import pytest
from validacao import validar_email

def test_email_valido():
    assert validar_email("laura@exemplo.com") == True

def test_email_sem_arroba():
    assert validar_email("laura.exemplo.com") == False

def test_email_sem_ponto_dominio():
    assert validar_email("laura@exemplo") == False

def test_email_multiplos_arroba():
    assert validar_email("laura@@exemplo.com") == False

def test_email_input_nao_string():
    assert validar_email(12345) == False