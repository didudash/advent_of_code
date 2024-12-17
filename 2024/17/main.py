def parse_input(file_path):
    with open(file_path) as f:
        reg_a = int(f.readline().split(":")[1])
        reg_b = int(f.readline().split(":")[1])
        reg_c = int(f.readline().split(":")[1])
        program = list(map(int, f.readlines()[1].split(":")[1].split(",")))
    return reg_a, reg_b, reg_c, program


def execute_program(a, b, c, program):
    out, ip = [], 0
    while ip < len(program):
        op, operand = program[ip], program[ip + 1]
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
    return out


def part_1(a, b, c, program):
    outputs = execute_program(a, b, c, program)
    return ",".join(map(str, outputs))


def part_2(program, registers_original):
    valid = [0]
    for length in range(1, len(program) + 1):
        oldvalid, valid = valid, []
        for num in oldvalid:
            for offset in range(8):
                newnum = 8 * num + offset
                outputs = execute_program(
                    newnum, registers_original["B"], registers_original["C"], program
                )
                if outputs == program[-length:]:
                    valid.append(newnum)
    return min(valid)


choose = {"p": "puzzle", "t": "toy"}.get("p")
file_path = f"{choose}_input.txt"
reg_a, reg_b, reg_c, program = parse_input(file_path)
registers_original = {"A": reg_a, "B": reg_b, "C": reg_c}

print(part_1(reg_a, reg_b, reg_c, program))
print(part_2(program, registers_original))
