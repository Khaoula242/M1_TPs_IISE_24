def add(a, b):
    """
    Additionne deux nombres.
    Args:
        a : Le premier nombre.
        b : Le second nombre.
    Returns:
        float: La somme des deux nombres.
    """
    return a + b

def subtract(a, b):
    """
    Soustrait le second nombre du premier.
    Args:
        a : Le premier nombre.
        b : Le second nombre.
    Returns:
        float: La différence entre les deux nombres.
    """
    return a - b

def multiply(a, b):
    """
    Multiplie deux nombres.
    Args:
        a : Le premier nombre.
        b : Le second nombre.
    Returns:
        float: Le produit des deux nombres.
    """
    return a * b

def divide(a, b):
    """
    Divise le premier nombre par le second.
    Args:
        a : Le numérateur.
        b : Le dénominateur.
    Returns:
        float: Le résultat de la division.
    Raises:
        ValueError: Si le dénominateur est zéro.
    """
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero is not allowed")
