""""
Name: João Victor Fernandes
Email: joao.victorfmaciel@gmail.com

    Codility Challenges Tests
"""

import pytest
import codility_challenges


binary = [(1041, 5),
          (32, 0),]


@pytest.mark.parametrize(['N', 'expected'], binary)
def test_binary_gap(N, expected):
    assert codility_challenges.binary_gap(N) == expected

cyclic = [([1, 2, 3, 4, 5], 4, [2, 3, 4, 5, 1]),
            ([0, 3, 5, 9], 3, [3, 5, 9, 0]),
            ([0, 0, 1], 3, [0, 0, 1]),
            ([5, 8, 7, 2, 4, 6, 9, 5], 6, [7, 2, 4, 6, 9, 5, 5, 8])]

@pytest.mark.parametrize(['A', 'K', 'expected'], cyclic)
def test_cyclic_rotation(A, K, expected):
    assert codility_challenges.cyclic_rotation(A, K) == expected

odd = [([1, 2, 3, 4, 4, 3, 2], 1),
       ([1, 2, 5, 6, 8, 3, 5, 4, 2, 5, 8, 1, 6, 3], 4),
       ([1, 1, 1, 1, 1, 1, 0, 1], 0)]

@pytest.mark.parametrize(['A', 'expected'], odd)
def test_odd_occurrences_in_array(A, expected):
    assert codility_challenges.odd_occurrences_in_array(A) == expected

coin = [([1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0 ,0, 1], 5),
        ([1, 1, 1, 1, 1, 1, 1], 3),
        ([0], 0),
        ([], 0)]

@pytest.mark.parametrize(['A', 'expected'], coin)
def test_coins(A, expected):
    assert codility_challenges.coins(A) == expected
