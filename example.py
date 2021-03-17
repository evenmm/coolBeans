def add(a, b):
    return a + b

def test_add():
    assert (add(0.1, 0.2) - 0.3) < 1e-6
    assert add('space', 'ship') == 'spaceship'

def substract(a, b):
    return a + b

def test_substract():
    assert abs(substract(2, 3) - (-1)) < 1e-10


