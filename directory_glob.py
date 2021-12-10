from pathlib import Path

path = Path()

for file in path.glob('*.py'): # search file 
    print(file)
