DATA_FILEPATH = "./input.data"

content = ""

with open(DATA_FILEPATH, "r") as file:
    content = file.read()

content: list[str] = content.split("\n")
bitmap = [[0 for _ in range(len(content[i]))] for i in range(len(content))]

# Trying all the ways
count = 0

# Horizontal
for i, line in enumerate(content):
    for j in range(len(line)):
        word = line[j:j+4]
        
        if word == "XMAS" or word[::-1] == "XMAS":
            count += 1
            for k in range(j, j+4):
                bitmap[i][k] = 1

# Vertical
# Transposing the content
vertical_content = ["" for _ in range(len(content[0]))]

for i in range(len(vertical_content)):
    for line in content:
        vertical_content[i] += line[i]

# Getting the count
for i, line in enumerate(vertical_content):
    for j in range(len(line)):
        word = line[j:j+4]
        
        if word == "XMAS" or word[::-1] == "XMAS":
            count += 1
            for k in range(j, j+4):
                bitmap[k][i] = 1

# Diagonal (to bottom-right)
for i in range(len(content) - 3):
    for j in range(len(content[i]) - 3):
        word = content[i][j] + content[i+1][j+1] + content[i+2][j+2] + content[i+3][j+3]
        
        if word == "XMAS" or word == "SAMX":
            count += 1
            bitmap[i][j] = 1
            bitmap[i+1][j+1] = 1
            bitmap[i+2][j+2] = 1
            bitmap[i+3][j+3] = 1

# Diagonal (to bottom-left)
for i in range(len(content) - 3):
    for j in range(len(content[i]) - 1, 2, -1):
        word = content[i][j] + content[i+1][j-1] + content[i+2][j-2] + content[i+3][j-3]
        
        if word == "XMAS" or word == "SAMX":
            count += 1
            bitmap[i][j] = 1
            bitmap[i+1][j-1] = 1
            bitmap[i+2][j-2] = 1
            bitmap[i+3][j-3] = 1

for i in range(len(bitmap)):
    for j in range(len(bitmap[i])):
        if bitmap[i][j]:
            print(content[i][j], end="")
        else:
            print(".", end="")
    print()
print(f"\nXMAS count: {count}")
