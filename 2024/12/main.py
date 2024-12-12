def read_map(filename):
    with open(filename, "r") as file:
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

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                letter = garden_map[r][c]
                area, perimeter = explore_region(r, c, letter, visited, rows, cols)
                regions.append((area, perimeter))

    return regions


def calculate_total_price(regions):
    return sum(area * perimeter for area, perimeter in regions)


def part_1(garden_map):
    regions = find_regions(garden_map)
    total_price = calculate_total_price(regions)
    print(total_price)


filename = "puzzle_input.txt"
garden_map = read_map(filename)
part_1(garden_map)
