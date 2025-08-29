with open("example.txt", "w") as f:
    f.write("hello world")

with open("data1.txt", "w") as f1:
    f1.write("first file content\n")

with open("data2.txt", "w") as f2:
    f2.write("second file content\n")

print("files written successfully")

import os

# Ensure input.txt exists
if not os.path.exists("input.txt"):
    with open("input.txt", "w") as f:
        f.write("Sample line 1\nSample line 2\n")

with open("input.txt", "r") as data, open("output.txt", "w") as output:
    for line in data:
        output.write(line.upper())
    print("processing done")

# Ensure numbers.txt exists
if not os.path.exists("numbers.txt"):
    with open("numbers.txt", "w") as f:
        f.write("1\n2\n3\n4\n5\n")

squares = []
with open("numbers.txt", "r") as r:
    nums = r.readlines()
    for n in nums:
        n = n.strip()
        if n.isdigit():
            squares.append(int(n) * int(n))

with open("squares.txt", "w") as f2:
    for sq in squares:
        f2.write(str(sq) + "\n")

print("squares written successfully")

