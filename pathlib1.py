from pathlib import Path

folder = Path("/Users/jaidevreddy/Documents/Documents - Jaidev’s MacBook Pro/python/test.txt")

print(folder.name + '\n')
print(folder.read_text())

print(folder.suffix + '\n')
print(folder.stem + '\n')


if not folder.exists():

    print("ffile does not exists")
else:
    print("file exists")