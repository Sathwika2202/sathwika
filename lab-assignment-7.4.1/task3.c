# Corrected version of the code

with open("example.txt", "w") as f:
    f.write("hello world")

with open("data1.txt", "w") as f1:
    f1.write("first file content\n")

with open("data2.txt", "w") as f2:
    f2.write("second file content\n")

print("files written successfully")

with open("input.txt", "r") as data:
    lines = data.readlines()

with open("output.txt", "w") as output:
    for line in lines:
        output.write(line.upper())

print("processing done")

with open("numbers.txt", "r") as r:
    nums = r.readlines()

squares = []
for n in nums:
    n = n.strip()
    if n.isdigit():
        squares.append(int(n) * int(n))

with open("squares.txt", "w") as f2:
    for sq in squares:
        f2.write(str(sq) + "\n")

print("squares written successfully")
