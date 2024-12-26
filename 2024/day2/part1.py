DATA_FILEPATH = "./input.data"

content = ""

with open(DATA_FILEPATH, "r") as file:
    content = file.read()

content = [[int(level) for level in line.split(" ")] for line in content.split("\n")]

def is_report_safe(report):
    positive_signal = report[1] - report[0] > 0

    valid_list = [1, 2, 3]
    if not positive_signal:
        valid_list = list(map(lambda x: -x, valid_list))

    for i in range(0, len(report) - 1):
        step = report[i + 1] - report[i]

        if step not in valid_list:
            return False

        if positive_signal and step < 0:
            return False
        
        if not positive_signal and step > 0:
            return False

        if report[i + 1] - report[i] != step:
            return False
    
    return True

safe_reports = 0

for report in content:
    if is_report_safe(report):
        safe_reports += 1

print(safe_reports)
