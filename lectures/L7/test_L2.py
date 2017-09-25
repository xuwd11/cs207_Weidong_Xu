import L2

def test_L2_result():
    assert L2.L2([3, 4]) == 5.0
    assert L2.L2([3, 4], [1, 1]) == 5
    
    
def test_L2_types():
    try:
        L2.L2(10)
    except TypeError as err:
        assert(type(err) == TypeError)

def test_L2_difflength():
    try:
        L2.L2([1, 1], [1, 1, 1])
    except ValueError as err:
        assert(type(err) == ValueError)