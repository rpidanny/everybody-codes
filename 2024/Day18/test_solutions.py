import os

import pytest
from solutions import part1, part2, part3

from utils.inputs import get_inputs

current_dir = os.path.dirname(os.path.realpath(__file__))

input = get_inputs(f"{current_dir}/input.txt")
input_2 = get_inputs(f"{current_dir}/input_2.txt")
input_3 = get_inputs(f"{current_dir}/input_3.txt")

input_test = get_inputs(f"{current_dir}/input_test.txt")
input_2_test = get_inputs(f"{current_dir}/input_2_test.txt")
input_3_test = get_inputs(f"{current_dir}/input_3_test.txt")


class TestPart1:
    def test_with_test_data(self):
        assert part1(input_test) == 11

    def test_with_real_data(self):
        assert part1(input) == 105


class TestPart2:
    def test_with_test_data(self):
        assert part2(input_2_test) == 21

    def test_with_real_data(self):
        assert part2(input_2) == 1341


class TestPart3:
    def test_with_test_data(self):
        assert part3(input_3_test) == 12

    def test_with_real_data(self):
        assert part3(input_3) == 293297
