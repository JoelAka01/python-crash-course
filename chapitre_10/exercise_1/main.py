from pathlib import Path

contents = Path('learning_python.txt').read_text()
lines = contents.splitlines()

# print(contents)
for line in lines:
    print(line)

