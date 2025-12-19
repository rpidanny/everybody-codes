import os
import sys

sys.path.append(".")

from solutions import part1, part2, part3

from utils.inputs import get_inputs
from utils.profiling import profile_run

if __name__ == "__main__":
    input_path = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    input_2_path = f"{os.path.dirname(os.path.realpath(__file__))}/input_2.txt"
    input_3_path = f"{os.path.dirname(os.path.realpath(__file__))}/input_3.txt"

    inputs = get_inputs(input_path)
    inputs_2 = get_inputs(input_2_path)
    inputs_3 = get_inputs(input_3_path)

    profile_run("Part 1", lambda: part1(inputs))
    profile_run("Part 2", lambda: part2(inputs_2))
    profile_run("Part 3", lambda: part3(inputs_3))
