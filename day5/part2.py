DATA_FILEPATH = "./input.data"

content = ""

with open(DATA_FILEPATH, "r") as file:
    content = file.read()


rule_list, updates = content.split("\n\n")
rule_list = [pair.split("|") for pair in rule_list.split("\n")]
updates = [ordering.split(",") for ordering in updates.split("\n")]

rule_dict = {}
for before, after in rule_list:
    if before not in rule_dict.keys():
        rule_dict[before] = [after]
    else:
        rule_dict[before].append(after)

def test_update(update: list[str]):
    reversed_update = update.copy()
    reversed_update.reverse()
    len_update = len(update)

    for page_index, page in enumerate(update):
        if page not in rule_dict.keys():
            continue

        for after in rule_dict[page]:
            if after not in reversed_update:
                continue

            after_index = len_update - reversed_update.index(after) - 1

            if after_index < page_index:
                return False
    
    return True


def get_middle_page(update: list[str]):
    if test_update(update):
        return 0
    
    print(update)

    while not test_update(update):
        for page_index, page in enumerate(update):
            if page not in rule_dict.keys():
                continue

            for after in rule_dict[page]:
                reversed_update = update.copy()
                reversed_update.reverse()

                if after not in update:
                    continue

                after_index = len(update) - reversed_update.index(after) - 1

                if after_index < page_index:
                    update[page_index] = update[after_index]
                    update[after_index] = page
    
    return int(update[len(update) // 2])


middle_page_sum = 0
for update in updates:
    middle_page_sum += get_middle_page(update)

print(middle_page_sum)
