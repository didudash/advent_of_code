def parse_input(file_path):
    with open(file_path) as f:
        reg_a = int(f.readline().split(":")[1])
        reg_b = int(f.readline().split(":")[1])
        reg_c = int(f.readline().split(":")[1])
        program = list(map(int, f.readlines()[1].split(":")[1].split(",")))
    return reg_a, reg_b, reg_c, program


def part_1(a, b, c, prog):
    out, ip = [], 0
    while ip < len(prog):
        op, operand = prog[ip], prog[ip + 1]
        match op:
            case 0:
                a //= 2 ** (operand if operand < 4 else [a, b, c][operand - 4])
            case 1:
                b ^= operand
            case 2:
                b = (operand if operand < 4 else [a, b, c][operand - 4]) % 8
            case 3:
                ip = operand if a != 0 else ip + 2
                continue
            case 4:
                b ^= c
            case 5:
                out.append((operand if operand < 4 else [a, b, c][operand - 4]) % 8)
            case 6:
                b = a // 2 ** (operand if operand < 4 else [a, b, c][operand - 4])
            case 7:
                c = a // 2 ** (operand if operand < 4 else [a, b, c][operand - 4])
        ip += 2
    return ",".join(map(str, out))


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"
a, b, c, program = parse_input(file_path)
print(part_1(a, b, c, program))
