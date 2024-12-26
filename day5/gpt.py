from collections import deque

def is_correct_order(rules, update):
    """
    Check if the pages in the update are in the correct order based on the rules.
    """
    # We will represent the pages and their dependencies as a directed graph.
    # Each rule X|Y means that X must come before Y.
    
    # Create a map of page dependencies
    graph = {page: set() for page in update}
    in_degree = {page: 0 for page in update}
    
    # Build the graph using the rules
    for rule in rules:
        x, y = map(int, rule.split('|'))
        if x in update and y in update:
            if y not in graph[x]:
                graph[x].add(y)
                in_degree[y] += 1
    
    # Perform a topological sort (Kahn's algorithm)
    order = []
    queue = deque([page for page in update if in_degree[page] == 0])
    
    while queue:
        page = queue.popleft()
        order.append(page)
        
        for neighbor in graph[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return order == update


def correct_order(rules, update):
    """
    Correct the order of pages in the update using the rules.
    """
    # We will represent the pages and their dependencies as a directed graph.
    graph = {page: set() for page in update}
    in_degree = {page: 0 for page in update}
    
    # Build the graph using the rules
    for rule in rules:
        x, y = map(int, rule.split('|'))
        if x in update and y in update:
            if y not in graph[x]:
                graph[x].add(y)
                in_degree[y] += 1
    
    # Perform a topological sort (Kahn's algorithm)
    order = []
    queue = deque([page for page in update if in_degree[page] == 0])
    
    while queue:
        page = queue.popleft()
        order.append(page)
        
        for neighbor in graph[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return order


def find_middle_page_number(update):
    """
    Find the middle page number from the update.
    """
    return update[len(update) // 2]


def main(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        data = file.read().strip().split("\n\n")
    
    # Split the rules and updates based on the input structure
    rules_input = data[0]
    updates_input = data[1]
    
    # Parse the rules and updates
    rules = rules_input.split('\n')
    updates = [list(map(int, update.split(','))) for update in updates_input.split('\n')]
    
    # Find the incorrectly ordered updates, correct them, and calculate the middle page numbers
    middle_page_numbers = []
    for update in updates:
        if not is_correct_order(rules, update):
            corrected_update = correct_order(rules, update)
            middle_page_numbers.append(find_middle_page_number(corrected_update))
    
    # Return the sum of the middle page numbers of corrected updates
    return sum(middle_page_numbers)


# Example usage
file_path = 'input.data'  # Change this to the path of your input file
result = main(file_path)
print("Sum of middle page numbers from corrected updates:", result)
