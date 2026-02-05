def total(liste):
    """ renvoie la somme des éléments d'une liste """

    result: float = 0.0
    if type(liste) is int:
        raise TypeError("total() argument must be a list, not int")
        return liste

    for item in liste:
        result += item

    return result
