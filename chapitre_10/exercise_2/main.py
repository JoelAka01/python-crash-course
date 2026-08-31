from pathlib import Path

contents = Path('learning_python.txt').read_text()
lines = contents.splitlines()
for line in lines:
    line = line.replace('python', 'C')
    print(line)
