from dsl import *


A = ((1, 0), (0, 1), (1, 0))
B = ((2, 1), (0, 1), (2, 1))
C = ((3, 4), (5, 5))
D = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
E = ((1, 2), (4, 5))
F = ((5, 6), (8, 0))
G = ((1, 0, 0, 0, 3), (0, 1, 1, 0, 0), (0, 1, 1, 2, 0), (0, 0, 2, 2, 0), (0, 2, 0, 0, 0))
H = ((0, 0, 0, 0, 0), (0, 2, 0, 2, 0), (2, 0, 0, 2, 0), (0, 0, 0, 0, 0), (0, 0, 2, 0, 0))
I = ((0, 0, 2, 0, 0), (0, 2, 0, 2, 0), (2, 0, 0, 2, 0), (0, 2, 0, 2, 0), (0, 0, 2, 0, 0))
J = ((0, 0, 2, 0, 0), (0, 2, 0, 2, 0), (0, 0, 2, 2, 0), (0, 2, 0, 2, 0), (0, 0, 2, 0, 0))
K = ((0, 0, 1, 0, 0, 1, 0, 0), (0, 0, 1, 0, 0, 1, 0, 0), (1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 1, 0, 0, 1, 0, 0), (0, 0, 1, 0, 0, 1, 0, 0), (1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 1, 0, 0, 1, 0, 0), (0, 0, 1, 0, 0, 1, 0, 0))


def test_identity():
    assert identity(1) == 1
 

def test_add():
    assert add(1, 2) == 3
    assert add(4, 6) == 10
 

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(4, 6) == -2
 

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(4, 3) == 12
 

def test_divide():
    assert divide(4, 2) == 2
    assert divide(9, 2) == 4
 

def test_invert():
    assert invert(1) == -1
    assert invert(-4) == 4
 

def test_even():
    assert not even(1)
    assert even(2)
 

def test_double():
    assert double(1) == 2
 

def test_halve():
    assert halve(2) == 1
    assert halve(5) == 2
 

def test_flip():
    assert flip(False)
    assert not flip(True)
 

def test_equality():
    assert equality(A, A)
    assert not equality(A, B)
 

def test_contained():
    assert contained(1, (1, 3))
    assert not contained(2, {3, 4})
 

def test_combine():
    assert combine(frozenset({1, 2}), frozenset({3, 4})) == frozenset({1, 2, 3, 4})
    assert combine((1, 2), (3, 4)) == (1, 2, 3, 4)
 

def test_intersection():
    assert intersection(frozenset({1, 2}), frozenset({2, 3})) == frozenset({2})
 

def test_difference():
    assert difference(frozenset({1, 2, 3}), frozenset({1, 2})) == frozenset({3})
 

def test_dedupe():
    assert dedupe((1, 2, 3, 3, 2, 4, 1)) == (1, 2, 3, 4)
 

def test_order():
    assert order(((1,), (1, 2, 3), (1, 2)), len) == ((1,), (1, 2), (1, 2, 3))
    assert order((1, 4, -3), abs) == (1, -3, 4)
 

def test_repeat():
    assert repeat(C, 3) == (C, C, C)
 

def test_greater():
    assert greater(2, 1)
    assert not greater(4, 10)
 

def test_size():
    assert size((1, 2, 3)) == 3
    assert size(frozenset({2, 5})) == 2
 

def test_merge():
    assert merge(frozenset({frozenset({(1, (0, 0))}), frozenset({(1, (1, 1)), (1, (0, 1))})})) == frozenset({(1, (0, 0)), (1, (1, 1)), (1, (0, 1))})
    assert merge(((1, 2), (3, 4, 5))) == (1, 2, 3, 4, 5)
    assert merge(((4, 5), (7,))) == (4, 5, 7)
 

def test_maximum():
    assert maximum({1, 2, 5, 3}) == 5
    assert maximum((4, 2, 6)) == 6
 

def test_minimum():
    assert minimum({1, 2, 5, 3}) == 1
    assert minimum((4, 2, 6)) == 2
 

def test_valmax():
    assert valmax(((1,), (1, 2)), len) == 2
 

def test_valmin():
    assert valmin(((1,), (1, 2)), len) == 1
 

def test_argmax():
    assert argmax(((1,), (1, 2)), len) == (1, 2)
 

def test_argmin():
    assert argmin(((1,), (1, 2)), len) == (1,)
 

def test_mostcommon():
    assert mostcommon((1, 2, 2, 3, 3, 3)) == 3
 

def test_leastcommon():
    assert leastcommon((1, 2, 3, 4, 2, 3, 4)) == 1
 

def test_initset():
    assert initset(2) == frozenset({2})
 

def test_both():
    assert not both(True, False)
    assert both(True, True)
    assert not both(False, False)
 

def test_either():
    assert either(True, False)
    assert either(True, True)
    assert not either(False, False)
 

def test_increment():
    assert increment(1) == 2
 

def test_decrement():
    assert decrement(1) == 0
 

def test_crement():
    assert crement(1) == 2
    assert crement(-2) == -3
 

def test_sign():
    assert sign(2) == 1
    assert sign(0) == 0
    assert sign(-1) == -1
 

def test_positive():
    assert positive(1)
    assert not positive(-2)
 

def test_toivec():
    assert toivec(2) == (2, 0)
 

def test_tojvec():
    assert tojvec(3) == (0, 3)
 

def test_sfilter():
    assert sfilter((1, 2, 3), lambda x: x > 1) == (2, 3)
    assert sfilter(frozenset({2, 3, 4}), lambda x: x % 2 == 0) == frozenset({2, 4})
 

def test_mfilter():
    assert mfilter(frozenset({frozenset({(2, (3, 3))}), frozenset({(1, (0, 0))}), frozenset({(1, (1, 1)), (1, (0, 1))})}), lambda x: len(x) == 1) == frozenset({(1, (0, 0)), (2, (3, 3))})
 

def test_extract():
    assert extract((1, 2, 3), lambda x: x > 2) == 3
    assert extract(frozenset({2, 3, 4}), lambda x: x % 4 == 0) == 4
 

def test_totuple():
    assert totuple({1}) == (1,)
 

def test_first():
    assert first((2, 3)) == 2
 

def test_last():
    assert last((2, 3)) == 3
 

def test_insert():
    assert insert(1, frozenset({2})) == frozenset({1, 2})
 

def test_remove():
    assert remove(1, frozenset({1, 2})) == frozenset({2})
 

def test_other():
    assert other({1, 2}, 1) == 2
 

def test_interval():
    assert interval(1, 4, 1) == (1, 2, 3)
    assert interval(5, 2, -1) == (5, 4, 3)
 

def test_astuple():
    assert astuple(3, 4) == (3, 4)
 

def test_product():
    assert product({1, 2}, {2, 3}) == frozenset({(1, 2), (1, 3), (2, 2), (2, 3)})
 

def test_pair():
    assert pair((1, 2), (4, 3)) == ((1, 4), (2, 3))
 

def test_branch():
    assert branch(True, 1, 3) == 1
    assert branch(False, 4, 2) == 2
 

def test_compose():
    assert compose(lambda x: x ** 2, lambda x: x + 1)(2) == 9
    assert compose(lambda x: x + 1, lambda x: x ** 2)(2) == 5
 

def test_chain():
    assert chain(lambda x: x + 3, lambda x: x ** 2, lambda x: x + 1)(2) == 12
 

def test_matcher():
    assert matcher(lambda x: x + 1, 3)(2)
    assert not matcher(lambda x: x - 1, 3)(2)
 

def test_rbind():
    assert rbind(lambda a, b: a + b, 2)(3) == 5
    assert rbind(lambda a, b: a == b, 2)(2)
 

def test_lbind():
    assert lbind(lambda a, b: a + b, 2)(3) == 5
    assert lbind(lambda a, b: a == b, 2)(2)
 

def test_power():
    assert power(lambda x: x + 1, 3)(4) == 7
 

def test_fork():
    assert fork(lambda x, y: x * y, lambda x: x + 1, lambda x: x + 2)(2) == 12
 

def test_apply():
    assert apply(lambda x: x ** 2, (1, 2, 3)) == (1, 4, 9)
    assert apply(lambda x: x % 2, frozenset({1, 2})) == frozenset({0, 1})
 

def test_rapply():
    assert rapply(frozenset({lambda x: x + 1, lambda x: x - 1}), 1) == {0, 2}
 

def test_mapply():
    assert mapply(lambda x: frozenset({(v + 1, (i, j)) for v, (i, j) in x}), frozenset({frozenset({(1, (0, 0))}), frozenset({(1, (1, 1)), (1, (0, 1))})})) == frozenset({(2, (0, 0)), (2, (1, 1)), (2, (0, 1))})
 

def test_papply():
    assert papply(lambda x, y: x + y, (1, 2), (3, 4)) == (4, 6)
 

def test_mpapply():
    assert mpapply(lambda x, y: frozenset({(x, (i, j)) for _, (i, j) in y}), (3, 4), frozenset({frozenset({(1, (0, 0))}), frozenset({(1, (1, 1)), (1, (0, 1))})})) == ((3, (0, 0)), (4, (1, 1)), (4, (0, 1)))
 

def test_prapply():
    assert prapply(lambda x, y: x + y, {1, 2}, {2, 3}) == frozenset({3, 4, 5})
 

def test_mostcolor():
    assert mostcolor(B) == 1
    assert mostcolor(C) == 5
 

def test_leastcolor():
    assert leastcolor(B) == 0
 

def test_height():
    assert height(A) == 3
    assert height(C) == 2
    assert height(frozenset({(0, 4)})) == 1
    assert height(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == 3
 

def test_width():
    assert width(A) == 2
    assert width(C) == 2
    assert width(frozenset({(0, 4)})) == 1
    assert width(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == 3
 

def test_shape():
    assert shape(A) == (3, 2)
    assert shape(C) == (2, 2)
    assert shape(frozenset({(0, 4)})) == (1, 1)
    assert shape(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == (3, 3)
 

def test_portrait():
    assert portrait(A)
    assert not portrait(C)
 

def test_colorcount():
    assert colorcount(A, 1) == 3
    assert colorcount(C, 5) == 2
    assert colorcount(frozenset({(1, (0, 0)), (2, (1, 0)), (2, (0, 1))}), 2) == 2
    assert colorcount(frozenset({(1, (0, 0)), (2, (1, 0)), (2, (0, 1))}), 1) == 1
 

def test_colorfilter():
     assert colorfilter(frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0))}), frozenset({(2, (4, 1))}), frozenset({(1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (3, 2)), (2, (2, 3)), (2, (3, 3))})}), 2) == frozenset({frozenset({(2, (4, 1))}), frozenset({(2, (3, 2)), (2, (2, 3)), (2, (3, 3))})})
 

def test_sizefilter():
    assert sizefilter(frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0))}), frozenset({(2, (4, 1))}), frozenset({(1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (3, 2)), (2, (2, 3)), (2, (3, 3))})}), 1) == frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0))}), frozenset({(2, (4, 1))})})
 

def test_asindices():
    assert asindices(A) == frozenset({(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)})
    assert asindices(C) == frozenset({(0, 0), (0, 1), (1, 0), (1, 1)})
 

def test_ofcolor():
    assert ofcolor(A, 0) == frozenset({(0, 1), (1, 0), (2, 1)})
    assert ofcolor(B, 2) == frozenset({(0, 0), (2, 0)})
    assert ofcolor(C, 1) == frozenset()
 

def test_ulcorner():
    assert ulcorner(frozenset({(1, 2), (0, 3), (4, 0)})) == (0, 0)
    assert ulcorner(frozenset({(1, 2), (0, 0), (4, 3)})) == (0, 0)
 

def test_urcorner():
    assert urcorner(frozenset({(1, 2), (0, 3), (4, 0)})) == (0, 3)
    assert urcorner(frozenset({(1, 2), (0, 0), (4, 3)})) == (0, 3)
 

def test_llcorner():
    assert llcorner(frozenset({(1, 2), (0, 3), (4, 0)})) == (4, 0)
    assert llcorner(frozenset({(1, 5), (0, 0), (2, 3)})) == (2, 0)
 

def test_lrcorner():
    assert lrcorner(frozenset({(1, 2), (0, 3), (4, 0)})) == (4, 3)
    assert lrcorner(frozenset({(1, 5), (0, 0), (2, 3)})) == (2, 5)
 

def test_crop():
    assert crop(A, (0, 0), (2, 2)) == ((1, 0), (0, 1))
    assert crop(C, (0, 1), (1, 1)) == ((4,),)
    assert crop(D, (1, 2), (2, 1)) == ((6,), (0,))
 

def test_toindices():
    assert toindices(frozenset({(1, (1, 1)), (1, (1, 0))})) == frozenset({(1, 1), (1, 0)})
    assert toindices(frozenset({(1, 1), (0, 1)})) == frozenset({(1, 1), (0, 1)})
 

def test_recolor():
    assert recolor(3, frozenset({(2, (0, 0)), (1, (0, 1)), (5, (1, 0))})) == frozenset({(3, (0, 0)), (3, (0, 1)), (3, (1, 0))})
    assert recolor(2, frozenset({(2, (2, 5)), (2, (1, 1))})) == frozenset({(2, (2, 5)), (2, (1, 1))})
 

def test_shift():
    assert shift(frozenset({(2, (1, 1)), (4, (1, 2)), (1, (2, 3))}), (1, 2)) == frozenset({(2, (2, 3)), (4, (2, 4)), (1, (3, 5))})
    assert shift(frozenset({(1, 3), (0, 2), (3, 4)}), (0, -1)) == frozenset({(1, 2), (0, 1), (3, 3)})
 

def test_normalize():
    assert normalize(frozenset({(2, (1, 1)), (4, (1, 2)), (1, (2, 3))})) == frozenset({(2, (0, 0)), (4, (0, 1)), (1, (1, 2))})
    assert normalize(frozenset({(1, 0), (0, 2), (3, 4)})) == frozenset({(1, 0), (0, 2), (3, 4)})
 

def test_dneighbors():
    assert dneighbors((1, 1)) == frozenset({(0, 1), (1, 0), (2, 1), (1, 2)})
    assert dneighbors((0, 0)) == frozenset({(0, 1), (1, 0), (-1, 0), (0, -1)})
    assert dneighbors((0, 1)) == frozenset({(0, 0), (1, 1), (-1, 1), (0, 2)})
    assert dneighbors((1, 0)) == frozenset({(0, 0), (1, 1), (1, -1), (2, 0)})
 

def test_ineighbors():
    assert ineighbors((1, 1)) == frozenset({(0, 0), (0, 2), (2, 0), (2, 2)})
    assert ineighbors((0, 0)) == frozenset({(1, 1), (-1, -1), (1, -1), (-1, 1)})
    assert ineighbors((0, 1)) == frozenset({(1, 0), (1, 2), (-1, 0), (-1, 2)})
    assert ineighbors((1, 0)) == frozenset({(0, 1), (2, -1), (2, 1), (0, -1)})
 

def test_neighbors():
    assert neighbors((1, 1)) == frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)})
    assert neighbors((0, 0)) == frozenset({(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)})
 

def test_objects():
    assert objects(G, True, False, True) == frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0))}), frozenset({(2, (4, 1))}), frozenset({(1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (3, 2)), (2, (2, 3)), (2, (3, 3))})})
    assert objects(G, True, True, True) == frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (4, 1)), (2, (3, 2)), (2, (2, 3)), (2, (3, 3))})})
    assert objects(G, False, False, True) == frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0))}), frozenset({(2, (4, 1))}), frozenset({(1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2)), (2, (3, 2)), (2, (2, 3)), (2, (3, 3))})})
    assert objects(G, False, True, True) == frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2)), (2, (4, 1)), (2, (3, 2)), (2, (2, 3)), (2, (3, 3))})})
    assert objects(G, True, False, False) == frozenset({frozenset({(3, (0, 4))}), frozenset({(1, (0, 0))}), frozenset({(2, (4, 1))}), frozenset({(1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (3, 2)), (2, (2, 3)), (2, (3, 3))}), frozenset({(0, (1, 0)), (0, (2, 0)), (0, (3, 0)), (0, (4, 0)), (0, (3, 1))}), frozenset({(0, (0, 1)), (0, (0, 2)), (0, (0, 3)), (0, (1, 3)), (0, (1, 4)), (0, (2, 4)), (0, (3, 4)), (0, (4, 4)), (0, (4, 3)), (0, (4, 2))})})
 

def test_partition():
    assert partition(B) == frozenset({frozenset({(0, (1, 0))}), frozenset({(2, (0, 0)), (2, (2, 0))}), frozenset({(1, (0, 1)), (1, (1, 1)), (1, (2, 1))})})
    assert partition(G) == frozenset({frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (4, 1)), (2, (3, 2)), (2, (2, 3)), (2, (3, 3))}), frozenset({(3, (0, 4))}), frozenset({(0, (0, 1)), (0, (0, 2)), (0, (0, 3)), (0, (1, 0)), (0, (1, 3)), (0, (1, 4)), (0, (2, 0)), (0, (2, 4)), (0, (3, 0)), (0, (3, 1)), (0, (3, 4)), (0, (4, 0)), (0, (4, 2)), (0, (4, 3)), (0, (4, 4))})})
 

def test_fgpartition():
    assert fgpartition(B) == frozenset({frozenset({(0, (1, 0))}), frozenset({(2, (0, 0)), (2, (2, 0))})})
    assert fgpartition(G) == frozenset({frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))}), frozenset({(2, (4, 1)), (2, (3, 2)), (2, (2, 3)), (2, (3, 3))}), frozenset({(3, (0, 4))})})
 

def test_uppermost():
    assert uppermost(frozenset({(0, 4)})) == 0
    assert uppermost(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == 0
 

def test_lowermost():
    assert lowermost(frozenset({(0, 4)})) == 0
    assert lowermost(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == 2
 

def test_leftmost():
    assert leftmost(frozenset({(0, 4)})) == 4
    assert leftmost(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == 0
 

def test_rightmost():
    assert rightmost(frozenset({(0, 4)})) == 4
    assert rightmost(frozenset({(1, (0, 0)), (1, (1, 1)), (1, (1, 2)), (1, (2, 1)), (1, (2, 2))})) == 2
 

def test_square():
    assert square(C)
    assert square(D)
    assert not square(A)
    assert not square(B)
    assert not square(frozenset({(1, 1), (1, 0)}))
    assert square(frozenset({(1, 1), (0, 0), (1, 0), (0, 1)}))
    assert not square(frozenset({(0, 0), (1, 0), (0, 1)}))
    assert square(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))}))
 

def test_vline():
    assert vline(frozenset({(1, (1, 1)), (1, (0, 1))}))
    assert not vline(frozenset({(1, 1), (1, 0)}))
 

def test_hline():
    assert hline(frozenset({(1, (1, 1)), (1, (1, 0))}))
    assert not hline(frozenset({(1, 1), (0, 1)}))
 

def test_hmatching():
    assert hmatching(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))}), frozenset({(1, (1, 3)), (2, (1, 4))}))
    assert not hmatching(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))}), frozenset({(1, (2, 3)), (2, (2, 4))}))
 

def test_vmatching():
    assert vmatching(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))}), frozenset({(1, (3, 1)), (2, (4, 1))}))
    assert not vmatching(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))}), frozenset({(1, (3, 2)), (2, (4, 2))}))
 

def test_manhattan():
    assert manhattan(frozenset({(0, 0), (1, 1)}), frozenset({(1, 2), (2, 3)})) == 1
    assert manhattan(frozenset({(1, 1)}), frozenset({(2, 3)})) == 3
 

def test_adjacent():
    assert adjacent(frozenset({(0, 0)}), frozenset({(0, 1), (1, 0)}))
    assert not adjacent(frozenset({(0, 0)}), frozenset({(1, 1)}))
 

def test_bordering():
    assert bordering(frozenset({(0, 0)}), D)
    assert bordering(frozenset({(0, 2)}), D)
    assert bordering(frozenset({(2, 0)}), D)
    assert bordering(frozenset({(2, 2)}), D)
    assert not bordering(frozenset({(1, 1)}), D)
 

def test_centerofmass():
    assert centerofmass(frozenset({(0, 0), (1, 1), (1, 2)})) == (0, 1)
    assert centerofmass(frozenset({(0, 0), (1, 1), (2, 2)})) == (1, 1)
    assert centerofmass(frozenset({(0, 0), (1, 1), (0, 1)})) == (0, 0)
 

def test_palette():
    assert palette(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))})) == frozenset({1, 2, 3})
    assert palette(frozenset({(1, (1, 1)), (1, (0, 0)), (1, (1, 0)), (1, (0, 1))})) == frozenset({1})
 

def test_numcolors():
    assert numcolors(frozenset({(1, (1, 1)), (2, (0, 0)), (2, (1, 0)), (3, (0, 1))})) == 3
    assert numcolors(frozenset({(1, (1, 1)), (1, (0, 0)), (1, (1, 0)), (1, (0, 1))})) == 1
 

def test_color():
    assert color(frozenset({(1, (1, 1)), (1, (0, 0)), (1, (1, 0)), (1, (0, 1))})) == 1
    assert color(frozenset({(2, (3, 1))})) == 2
 

def test_toobject():
    assert toobject(frozenset({(0, 0), (0, 2)}), G) == frozenset({(1, (0, 0)), (0, (0, 2))})
    assert toobject(frozenset({(0, 4)}), G) == frozenset({(3, (0, 4))})
 

def test_asobject():
    assert asobject(A) == frozenset({(0, (0, 1)), (0, (1, 0)), (0, (2, 1)), (1, (0, 0)), (1, (1, 1)), (1, (2, 0))})
 

def test_rot90():
    assert rot90(B) == ((2, 0, 2), (1, 1, 1))
    assert rot90(C) == ((5, 3), (5, 4))
 

def test_rot180():
    assert rot180(B) == ((1, 2), (1, 0), (1, 2))
    assert rot180(C) == ((5, 5), (4, 3))
 

def test_rot270():
    assert rot270(B) == ((1, 1, 1), (2, 0, 2))
    assert rot270(C) == ((4, 5), (3, 5))
 

def test_hmirror():
    assert hmirror(B) == ((2, 1), (0, 1), (2, 1))
    assert hmirror(C) == ((5, 5), (3, 4))
    assert hmirror(frozenset({(0, 0), (1, 1)})) == frozenset({(1, 0), (0, 1)})
    assert hmirror(frozenset({(0, 0), (1, 0), (1, 1)})) == frozenset({(1, 0), (0, 1), (0, 0)})
    assert hmirror(frozenset({(0, 1), (1, 2)})) == frozenset({(0, 2), (1, 1)})
 

def test_vmirror():
    assert vmirror(B) == ((1, 2), (1, 0), (1, 2))
    assert vmirror(C) == ((4, 3), (5, 5))
    assert vmirror(frozenset({(0, 0), (1, 1)})) == frozenset({(1, 0), (0, 1)})
    assert vmirror(frozenset({(0, 0), (1, 0), (1, 1)})) == frozenset({(1, 0), (1, 1), (0, 1)})
    assert vmirror(frozenset({(0, 1), (1, 2)})) == frozenset({(0, 2), (1, 1)})
 

def test_dmirror():
    assert dmirror(B) == ((2, 0, 2), (1, 1, 1))
    assert dmirror(C) == ((3, 5), (4, 5))
    assert dmirror(frozenset({(0, 0), (1, 1)})) == frozenset({(0, 0), (1, 1)})
    assert dmirror(frozenset({(0, 0), (1, 0), (1, 1)})) == frozenset({(0, 1), (1, 1), (0, 0)})
    assert dmirror(frozenset({(0, 1), (1, 2)})) == frozenset({(0, 1), (1, 2)})
 

def test_cmirror():
    assert cmirror(B) == ((1, 1, 1), (2, 0, 2))
    assert cmirror(C) == ((5, 4), (5, 3))
    assert cmirror(frozenset({(0, 0), (1, 1)})) == frozenset({(0, 0), (1, 1)})
    assert cmirror(frozenset({(0, 0), (1, 0), (1, 1)})) == frozenset({(0, 0), (1, 0), (1, 1)})
    assert cmirror(frozenset({(0, 1), (1, 2)})) == frozenset({(0, 1), (1, 2)})
 

def test_fill():
    assert fill(B, 3, frozenset({(0, 0), (1, 1)})) == ((3, 1), (0, 3), (2, 1))
    assert fill(C, 1, frozenset({(1, 0)})) == ((3, 4), (1, 5))
 

def test_paint():
    assert paint(B, frozenset({(1, (0, 0)), (2, (1, 1))})) == ((1, 1), (0, 2), (2, 1))
    assert paint(C, frozenset({(6, (1, 0))})) == ((3, 4), (6, 5))
 

def test_underfill():
    assert underfill(C, 1, frozenset({(0, 0), (1, 0)})) == ((3, 4), (1, 5))
 

def test_underpaint():
    assert underpaint(B, frozenset({(3, (0, 0)), (3, (1, 1))})) == ((2, 1), (0, 3), (2, 1))
    assert underpaint(C, frozenset({(3, (1, 1))})) == ((3, 4), (5, 3))
 

def test_hupscale():
    assert hupscale(B, 1) == B
    assert hupscale(C, 1) == C
    assert hupscale(B, 2) == ((2, 2, 1, 1), (0, 0, 1, 1), (2, 2, 1, 1))
    assert hupscale(C, 2) == ((3, 3, 4, 4), (5, 5, 5, 5))
 

def test_vupscale():
    assert vupscale(B, 1) == B
    assert vupscale(C, 1) == C
    assert vupscale(B, 2) == ((2, 1), (2, 1), (0, 1), (0, 1), (2, 1), (2, 1))
    assert vupscale(C, 2) == ((3, 4), (3, 4), (5, 5), (5, 5))
 

def test_upscale():
    assert upscale(B, 1) == B
    assert upscale(C, 1) == C
    assert upscale(B, 2) == ((2, 2, 1, 1), (2, 2, 1, 1), (0, 0, 1, 1), (0, 0, 1, 1), (2, 2, 1, 1), (2, 2, 1, 1))
    assert upscale(C, 2) == ((3, 3, 4, 4), (3, 3, 4, 4), (5, 5, 5, 5), (5, 5, 5, 5))
    assert upscale(frozenset({(3, (0, 1)), (4, (1, 0)), (5, (1, 1))}), 2) == frozenset({(3, (0, 2)), (3, (0, 3)), (3, (1, 2)), (3, (1, 3)), (4, (2, 0)), (4, (3, 0)), (4, (2, 1)), (4, (3, 1)), (5, (2, 2)), (5, (3, 2)), (5, (2, 3)), (5, (3, 3))})
    assert upscale(frozenset({(3, (0, 0))}), 2) == frozenset({(3, (0, 0)), (3, (1, 0)), (3, (0, 1)), (3, (1, 1))})
 

def test_downscale():
    assert downscale(B, 1) == B
    assert downscale(C, 1) == C
    assert downscale(((2, 2, 1, 1), (2, 2, 1, 1), (0, 0, 1, 1), (0, 0, 1, 1), (2, 2, 1, 1), (2, 2, 1, 1)), 2) == B
    assert downscale(((3, 3, 4, 4), (3, 3, 4, 4), (5, 5, 5, 5), (5, 5, 5, 5)), 2) == C
 

def test_hconcat():
    assert hconcat(A, B) == ((1, 0, 2, 1), (0, 1, 0, 1), (1, 0, 2, 1))
    assert hconcat(B, A) == ((2, 1, 1, 0), (0, 1, 0, 1), (2, 1, 1, 0))
 

def test_vconcat():
    assert vconcat(A, B) == ((1, 0), (0, 1), (1, 0), (2, 1), (0, 1), (2, 1))
    assert vconcat(B, A) == ((2, 1), (0, 1), (2, 1), (1, 0), (0, 1), (1, 0))
    assert vconcat(B, C) == ((2, 1), (0, 1), (2, 1), (3, 4), (5, 5))
 

def test_subgrid():
    assert subgrid(frozenset({(3, (0, 0))}), C) == ((3,),)
    assert subgrid(frozenset({(5, (1, 0)), (5, (1, 1))}), C) == ((5, 5),)
    assert subgrid(frozenset({(2, (0, 1)), (4, (1, 0))}), D) == ((1, 2), (4, 5))
    assert subgrid(frozenset({(1, (0, 0)), (0, (2, 2))}), D) == D
 

def test_hsplit():
    assert hsplit(B, 1) == (B,)
    assert hsplit(B, 2) == (((2,), (0,), (2,)), ((1,), (1,), (1,)))
    assert hsplit(C, 1) == (C,)
    assert hsplit(C, 2) == (((3,), (5,)), ((4,), (5,)))
 

def test_vsplit():
    assert vsplit(B, 1) == (B,)
    assert vsplit(B, 3) == (((2, 1),), ((0, 1),), ((2, 1),))
    assert vsplit(C, 1) == (C,)
    assert vsplit(C, 2) == (((3, 4),), ((5, 5),))
 

def test_cellwise():
    assert cellwise(A, B, 0) == ((0, 0), (0, 1), (0, 0))
    assert cellwise(C, E, 0) == ((0, 0), (0, 5))
 

def test_replace():
    assert replace(B, 2, 3) == ((3, 1), (0, 1), (3, 1))
    assert replace(C, 5, 0) == ((3, 4), (0, 0))
 

def test_switch():
    assert switch(C, 3, 4) == ((4, 3), (5, 5))
 

def test_center():
    assert center(frozenset({(1, (0, 0))})) == (0, 0)
    assert center(frozenset({(1, (0, 0)), (1, (0, 2))})) == (0, 1)
    assert center(frozenset({(1, (0, 0)), (1, (0, 2)), (1, (2, 0)), (1, (2, 2))})) == (1, 1)
 

def test_position():
    assert position(frozenset({(0, (1, 1))}), frozenset({(0, (2, 2))})) == (1, 1)
    assert position(frozenset({(0, (2, 2))}), frozenset({(0, (1, 2))})) == (-1, 0)
    assert position(frozenset({(0, (3, 3))}), frozenset({(0, (3, 4))})) == (0, 1)
 

def test_index():
    assert index(C, (0, 0)) == 3
    assert index(D, (1, 2)) == 6
 

def test_canvas():
    assert canvas(3, (1, 2)) == ((3, 3),)
    assert canvas(2, (3, 1)) == ((2,), (2,), (2,))
 

def test_corners():
    assert corners(frozenset({(1, 2), (0, 3), (4, 0)})) == frozenset({(0, 0), (0, 3), (4, 0), (4, 3)})
    assert corners(frozenset({(1, 2), (0, 0), (4, 3)})) == frozenset({(0, 0), (0, 3), (4, 0), (4, 3)})
 

def test_connect():
    assert connect((1, 1), (2, 2)) == frozenset({(1, 1), (2, 2)})
    assert connect((1, 1), (1, 4)) == frozenset({(1, 1), (1, 2), (1, 3), (1, 4)})
 

def test_cover():
    assert cover(C, frozenset({(0, 0)})) == ((5, 4), (5, 5))
 

def test_trim():
    assert trim(D) == ((5,),)
 

def test_move():
    assert move(C, frozenset({(3, (0, 0))}), (1, 1)) == ((5, 4), (5, 3))
 

def test_tophalf():
    assert tophalf(C) == ((3, 4),)
    assert tophalf(D) == ((1, 2, 3),)
 

def test_bottomhalf():
    assert bottomhalf(C) == ((5, 5),)
    assert bottomhalf(D) == ((7, 8, 0),)
 

def test_lefthalf():
    assert lefthalf(C) == ((3,), (5,))
    assert lefthalf(D) == ((1,), (4,), (7,))
 

def test_righthalf():
    assert righthalf(C) == ((4,), (5,))
    assert righthalf(D) == ((3,), (6,), (0,))
 

def test_vfrontier():
    assert vfrontier((3, 4)) == frozenset({(i, 4) for i in range(30)})
 

def test_hfrontier():
    assert hfrontier((3, 4)) == frozenset({(3, i) for i in range(30)})
 

def test_backdrop():
    assert backdrop(frozenset({(2, 3), (3, 2), (3, 3), (4, 1)})) == frozenset({(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3),})
 

def test_delta():
    assert delta(frozenset({(2, 3), (3, 2), (3, 3), (4, 1)})) == frozenset({(2, 1), (2, 2), (3, 1), (4, 2), (4, 3)})
 

def test_gravitate():
    assert gravitate(frozenset({(0, 0)}), frozenset({(0, 1)})) == (0, 0)
    assert gravitate(frozenset({(0, 0)}), frozenset({(0, 4)})) == (0, 3)
 

def test_inbox():
    assert inbox(frozenset({(0, 0), (2, 2)})) == frozenset({(1, 1)})
 

def test_outbox():
    assert outbox(frozenset({(1, 1)})) == frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)})
 

def test_box():
    assert box(frozenset({(0, 0), (1, 1)})) == frozenset({(0, 0), (0, 1), (1, 0), (1, 1)})
 

def test_shoot():
    assert shoot((0, 0), (1, 1)) == frozenset({(i, i) for i in range(43)})
 

def test_occurrences():
    assert occurrences(G, frozenset({(1, (0, 0)), (1, (0, 1))})) == frozenset({(1, 1), (2, 1)})
 

def test_frontiers():
    assert frontiers(C) == frozenset({frozenset({(5, (1, 0)), (5, (1, 1))})})
 

def test_compress():
    assert compress(K) == ((0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0))
 

def test_hperiod():
    assert hperiod(frozenset({(8, (2, 1)), (8, (1, 3)), (2, (2, 4)), (8, (2, 3)), (2, (2, 2)), (2, (1, 2)), (8, (1, 1)), (8, (1, 5)), (2, (1, 4)), (8, (2, 5)), (2, (2, 0)), (2, (1, 0))})) == 2
    assert hperiod(frozenset({(2, (2, 6)), (2, (2, 0)), (3, (2, 4)), (3, (2, 2)), (3, (2, 5)), (2, (2, 3)), (3, (2, 1))})) == 3
 

def test_vperiod():
    assert vperiod(frozenset({(2, (2, 6)), (2, (2, 0)), (3, (2, 4)), (3, (2, 2)), (3, (2, 5)), (2, (2, 3)), (3, (2, 1))})) == 1
    assert vperiod(frozenset({(1, (2, 6)), (2, (3, 5)), (2, (3, 0)), (2, (2, 2)), (2, (2, 7)), (1, (3, 4)), (2, (2, 1)), (1, (2, 3)), (2, (2, 5)), (2, (2, 4)), (1, (3, 7)), (1, (2, 0)), (2, (3, 6)), (2, (3, 2)), (2, (3, 3)), (1, (3, 1))})) == 2
