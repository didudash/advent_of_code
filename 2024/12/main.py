def read_map(file_name):
    with open(file_name, "r") as file:
        return [list(line.strip()) for line in file]


def explore_region(r, c, letter, visited, rows, cols):
    stack = [(r, c)]
    area = 0
    perimeter = 0

    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue

        visited[x][y] = True
        area += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if garden_map[nx][ny] == letter and not visited[nx][ny]:
                    stack.append((nx, ny))
                elif garden_map[nx][ny] != letter:
                    perimeter += 1
            else:
                perimeter += 1

    return area, perimeter


def find_regions(garden_map):
    rows, cols = len(garden_map), len(garden_map[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                letter = garden_map[r][c]
                region_boundaries = {direction: set() for direction in directions}
                stack = [(r, c)]
                area = 0

                while stack:
                    x, y = stack.pop()
                    if visited[x][y]:
                        continue

                    visited[x][y] = True
                    area += 1

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols:
                            if garden_map[nx][ny] == letter and not visited[nx][ny]:
                                stack.append((nx, ny))
                            elif garden_map[nx][ny] != letter:
                                region_boundaries[(dx, dy)].add((x, y))
                        else:
                            region_boundaries[(dx, dy)].add((x, y))

                regions.append((area, region_boundaries))

    return regions


def calculate_total_price_part_1(regions):
    return sum(
        area * sum(len(boundary_cells) for boundary_cells in boundaries.values())
        for area, boundaries in regions
    )


def calculate_total_price_part_2(regions):
    total_price = 0

    for area, boundaries in regions:
        sides = 0

        for direction, boundary_cells in boundaries.items():
            previous_cell = (-1, -1)
            is_horizontal = direction in [(1, 0), (-1, 0)]
            sorted_cells = sorted(
                boundary_cells,
                key=lambda p: (p[0], p[1]) if is_horizontal else (p[1], p[0]),
            )

            for cell in sorted_cells:
                sides += 1
                if previous_cell != (-1, -1) and (
                    (cell[1] == previous_cell[1] + 1 and cell[0] == previous_cell[0])
                    if is_horizontal
                    else (
                        cell[0] == previous_cell[0] + 1 and cell[1] == previous_cell[1]
                    )
                ):
                    sides -= 1
                previous_cell = cell

        total_price += sides * area

    return total_price


def part_1(garden_map):
    regions = find_regions(garden_map)
    total_price = calculate_total_price_part_1(regions)
    print(total_price)


def part_2(garden_map):
    regions = find_regions(garden_map)
    total_price = calculate_total_price_part_2(regions)
    print(total_price)


file_name = "puzzle_input.txt"
garden_map = read_map(file_name)
part_1(garden_map)
part_2(garden_map)
