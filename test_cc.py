import pytest
from cc import change

def test_no_coins():
    assert change(0) == []

def test_1p_coin():
    assert change(1) == [1]

def test_2p_coin():
    assert change(2) == [2]

def test_1p_and_a_2p_coin():
    assert change(3) == [1, 2]

def test_5p_coin():
    assert change(5) == [5]

def test_5p_and_a_1p_coin():
    assert change(6) == [1, 5]

@pytest.mark.skip
def test_10p():
    assert change(10) == [10]

@pytest.mark.parametrize('coin', [10, 20, 50, 100, 200])
def test_all_coins(coin):
    assert change(coin) == [coin]
