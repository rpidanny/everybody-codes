from collections import defaultdict

from pyparsing import deque

UP = (0, 1)
DOWN = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)
UP_RIGHT = (1, 1)
UP_LEFT = (-1, 1)
DOWN_RIGHT = (1, -1)
DOWN_LEFT = (-1, -1)

BASIC_DIRECTIONS = [UP, DOWN, RIGHT, LEFT]

ALL_DIRECTIONS = [
    UP,
    DOWN,
    RIGHT,
    LEFT,
    UP_RIGHT,
    UP_LEFT,
    DOWN_RIGHT,
    DOWN_LEFT,
]


def get_starting_point(inputs: list[str]) -> tuple[int, int]:
    m, n = len(inputs), len(inputs[0])

    # first and last col
    cols = [0, n - 1]
    for r in range(m):
        for c in cols:
            if inputs[r][c] == ".":
                return (r, c)

    # first and last row
    rows = [0, m - 1]
    for c in range(n):
        for r in rows:
            if inputs[r][c] == ".":
                return (r, c)


def get_starting_points(inputs: list[str]) -> list[tuple[int, int]]:
    m, n = len(inputs), len(inputs[0])

    res = []

    # first and last col
    cols = [0, n - 1]
    for r in range(m):
        for c in cols:
            if inputs[r][c] == ".":
                res.append((r, c))

    # first and last row
    rows = [0, m - 1]
    for c in range(n):
        for r in rows:
            if inputs[r][c] == ".":
                res.append((r, c))

    return res


def get_tree_count(inputs: list[str]) -> int:
    # m, n = len(inputs), len(inputs[0])

    # tree_count = 0
    # for r in range(m):
    #     for c in range(n):
    #         if inputs[r][c] == "P":
    #             tree_count += 1
    # return tree_count

    return "".join(inputs).count("P")


def get_tree_positions(inputs: list[str]) -> list[tuple[int, int]]:
    m, n = len(inputs), len(inputs[0])
    res = []
    for r in range(m):
        for c in range(n):
            if inputs[r][c] == "P":
                res.append((r, c))
    return res


def part1(inputs: list[str]) -> int:
    m, n = len(inputs), len(inputs[0])

    tree_count = get_tree_count(inputs)
    r, c = get_starting_point(inputs)

    queue = deque([(r, c)])
    depth, visited = 0, set([(r, c)])

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            if inputs[r][c] == "P":
                tree_count -= 1
            if not tree_count:
                return depth

            for dr, dc in BASIC_DIRECTIONS:
                nr, nc = r + dr, c + dc
                if (
                    (nr, nc) not in visited
                    and 0 <= nr < m
                    and 0 <= nc < n
                    and inputs[nr][c] != "#"
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        depth += 1

    return depth


def part2(inputs: list[str]) -> int:
    m, n = len(inputs), len(inputs[0])

    tree_count = get_tree_count(inputs)
    starting_points = get_starting_points(inputs)

    queue = deque(starting_points)
    depth, visited = 0, set(starting_points)

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            if inputs[r][c] == "P":
                tree_count -= 1
            if not tree_count:
                return depth

            for dr, dc in BASIC_DIRECTIONS:
                nr, nc = r + dr, c + dc
                if (
                    (nr, nc) not in visited
                    and 0 <= nr < m
                    and 0 <= nc < n
                    and inputs[nr][c] != "#"
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        depth += 1

    return depth


def part3(inputs: list[str]) -> int:
    m, n = len(inputs), len(inputs[0])

    tree_positions = get_tree_positions(inputs)
    d = defaultdict(int)

    for tree in tree_positions:
        queue = deque([tree])
        visited = set([tree])
        depth = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if inputs[r][c] != "P":
                    d[(r, c)] += depth

                for dr, dc in BASIC_DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m
                        and 0 <= nc < n
                        and (nr, nc) not in visited
                        and inputs[nr][nc] != "#"
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            depth += 1

    return min(d.values())
