import pytest
from code1 import total


def test_total():
    # Vérifie le fonctionnement de base :
    assert total([1, 2, 3]) == 6

    # Vérifie que la somme marche avec un nombre négatif et un positif :
    assert total([1, -1]) == 0

    # Vérifie que la somme marche avec deux négatifs :
    assert total([-1, -1]) == -2

    # Vérifie que la somme marche avec un seul élément :
    assert total([1]) == 1

    # Vérifie que la liste vide renvoie bien 0 :
    assert total([]) == 0


def test_total_raises_exception_on_non_list_arguments():
    with pytest.raises(TypeError):
        x = total(1)
        print("total(1) type error : ", x)


print(test_total())
