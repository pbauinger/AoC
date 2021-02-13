from pathlib import Path
from sympy.ntheory.modular import crt

data = Path("input.txt").read_text().splitlines()[1].split(',')
data = [(int(val), idx) for (idx, val) in enumerate(data) if val != 'x']

print(crt([id for id, _ in data], [-offset for _, offset in data]))
