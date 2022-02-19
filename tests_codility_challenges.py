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
