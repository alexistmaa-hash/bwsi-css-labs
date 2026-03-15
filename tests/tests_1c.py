"""
tests_1c.py

Unit tests for `max_subarray_sum` in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum


def test_example_case():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_sum(nums) == 6


def test_all_negative():
    nums = [-8, -3, -6, -2, -5, -4]
    assert max_subarray_sum(nums) == -2


def test_single_element():
    assert max_subarray_sum([5]) == 5
    assert max_subarray_sum([-5]) == -5


def test_mixed_numbers():
    assert max_subarray_sum([1, 2, 3, -2, 5]) == 9
    assert max_subarray_sum([2, -1, 2, 3, 4, -5]) == 10


def test_empty_list_raises():
    with pytest.raises(ValueError):
        max_subarray_sum([])


if __name__ == "__main__":
    pytest.main()
