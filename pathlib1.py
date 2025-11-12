from pathlib import Path

folder = Path("/Users/jaidevreddy/Documents/Documents - Jaidev’s MacBook Pro/python/test.txt")

print(folder.name + '\n')
print(folder.read_text())

print(folder.suffix + '\n')
print(folder.stem + '\n')