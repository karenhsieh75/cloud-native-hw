from square_sum import square_sum

def test_square_sum_normal():
    assert square_sum([1, 2, 3]) == 14

def test_square_sum_empty():
    assert square_sum([]) == 0

def test_square_sum_negative():
    assert square_sum([-1, -2]) == 5