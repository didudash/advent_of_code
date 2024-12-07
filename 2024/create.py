import os, sys

if len(sys.argv) < 2:
    print("Usage: provide day after script")
else:
    day = sys.argv[1]
    os.makedirs(day, exist_ok=True)
    for f in ["main.py", "puzzle_input.txt", "toy_input.txt"]:
        open(os.path.join(day, f), "w").close()
    print(f"Created folder '{day}' with files.")
