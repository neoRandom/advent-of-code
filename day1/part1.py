DATA_FILEPATH = "./data.csv"

with open(DATA_FILEPATH, "r") as file:
    content = file.read()

content = [line.split(",") for line in content.split("\n") if line.count(",") == 1]

list_a = []
list_b = []

for item_a, item_b in content:
    list_a.append(int(item_a))
    list_b.append(int(item_b))

# Real part
list_a.sort()
list_b.sort()

distance = 0

for item_a, item_b in zip(list_a, list_b):
    distance += abs(item_a - item_b)

print(distance)
