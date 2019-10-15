import foo

def test_solve_quadratic():
    
    assert(foo.solve_quadratic(1,0,-1)==(-1.0,1.0))
    assert(foo.solve_quadratic(1,0,0)==5.0)
    assert(foo.solve_quadratic(1,0,1) is None)