def unique_items(item_list):
    return list(set(item_list))

user_entries = input("Enter a list of items separated by spaces: ").split()
unique_list = unique_items(user_entries)
print("Your list without duplicates is:", unique_list)
