
from pathlib import Path
BASE_DIR = str(Path(__file__).resolve().parent.parent)
with open(f"{BASE_DIR}\\BASE_DIR.txt",'r') as file:
    data = (file.read()).split('\n')
p1 = f"start {data[3]}" + "\n" + f"{data[1]} {data[2]}"
p2 =f"{data[3]} -s stop"
try:
    with open(f"{BASE_DIR}\\RUN.bat",'x') as f:
        f.write(p1)
    with open(f"{BASE_DIR}\\STOP.bat",'x') as f:
        f.write(p2)
except Exception as e:
    with open(f"{BASE_DIR}\\RUN.bat",'w') as f:
        f.write(p1)
    with open(f"{BASE_DIR}\\STOP.bat",'w') as f:
        f.write(p2)
