import dis
import marshal

with open("__pycache__/fibonacci.cpython-311.pyc", "rb") as f:
    _ = f.read(16)  # Skip the 16-byte header
    loaded = marshal.load(f)
    dis.dis(loaded)
