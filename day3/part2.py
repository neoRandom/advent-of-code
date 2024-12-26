DATA_FILEPATH = "./input.data"

raw_content: str = ""

with open(DATA_FILEPATH, "r") as file:
    raw_content = file.read()

# Deleting what is not necessary
content = ""
insert_mode = False
paused = False

i = 0
while i < len(raw_content):
    # Testing for do's and dont's
    if raw_content[i:i+4] == "do()":
        paused = False
        i += 4
    if raw_content[i:i+7] == "don't()":
        paused = True
        i += 7

    if not insert_mode and raw_content[i:i+4] == "mul(":
        insert_mode = True

        # Test if the ( is closed
        for j in range(i + 4, len(raw_content)):
            char = raw_content[j]
            if char == ")":
                break
            if char not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ","):
                insert_mode = False
    
    char = raw_content[i]

    if insert_mode and not paused:
        content += char

    if char == ")":
        content += " "
        insert_mode = False
    
    i += 1

print(content)

# Parsing the multiplication
content = [pair.split(",") for pair in content.replace("mul(", "").replace(")", "").split(" ") if pair.count(",") == 1]
print(content)

result = sum(map(lambda pair: int(pair[0]) * int(pair[1]), content))

print(result)
