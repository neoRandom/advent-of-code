DATA_FILEPATH = "./input.data"

content = ""

with open(DATA_FILEPATH, "r") as file:
    content = file.read()

content: list[str] = content.split("\n")
bitmap = [[0 for _ in range(len(content[i]))] for i in range(len(content))]

# Trying all the ways
count = 0

for i in range(len(content) - 2):
    for j in range(len(content[i]) - 2):
        if content[i+1][j+1] != "A":
            continue
        # M M
        #  A
        # S S
        # 1 2
        #  X
        # 4 5
        word = content[i][j] + content[i+2][j] + content[i][j+2] + content[i+2][j+2]
        
        if word in ("MMSS", "MSMS", "SSMM", "SMSM"):
            count += 1
            bitmap[i][j] = 1
            bitmap[i+2][j] = 1
            bitmap[i+1][j+1] = 1
            bitmap[i][j+2] = 1
            bitmap[i+2][j+2] = 1


for i in range(len(bitmap)):
    for j in range(len(bitmap[i])):
        if bitmap[i][j]:
            print(content[i][j], end="")
        else:
            print(".", end="")
    print()

print(f"\nX-MAS count: {count}")
