def remove_name(name_list, name):
    n = []
    for item in l:
        if (item != name):
            n.append(item.strip(name))
    return n

l = ["Ram", "Shyam", "Mohan"]
print(remove_name(l, "R"))  # Example usage to remove "Ram" from the list