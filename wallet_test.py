
import pytest
from wallet import Wallet, InsufficientAmount


def test_default_initial_amount():
    # un portefeuille nouvellement créé a une balance de 0
    my_wallet = Wallet()
    assert my_wallet.balance == 0


def test_setting_initial_amount():
    # un portefeuille créé avec une balance initiale de 100 a bien une balance
    # de 100
    my_wallet = Wallet(100)
    assert my_wallet.balance == 100


def test_wallet_add_cash():
    # un portefeuille créé avec une balance initiale de 10 auquel on ajoute 90
    # a une balance de 100
    my_wallet = Wallet(10)
    my_wallet.add_cash(90)
    assert my_wallet.balance == 100


def test_wallet_spend_cash():
    # un portefeuille créé avec une balance initiale de 20 auquel on ôte 10 a
    # une balance de 10
    my_wallet = Wallet(20)
    my_wallet.withdraw(10)
    assert my_wallet.balance == 10


def test_raise_exception_Inssuficiant_Amount():
    # un portefeuille qui essaie de dépenser plus que sa balance va provoquer
    # une erreur InsufficientAmount
    my_wallet = Wallet(20)
    with pytest.raises(InsufficientAmount):
        my_wallet.spend_cash(100)
