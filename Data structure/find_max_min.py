def find_max_min():
    numbers = [int(x) for x in input("Please enter your numbers (separated by spaces): ").split()]
    if not numbers:
        print("No numbers were entered.")
        return None
    return max(numbers), min(numbers)

result = find_max_min()
if result:
    max_num, min_num = result
    print(f"Maximum number is: {max_num}")
    print(f"Minimum number is: {min_num}")
    print("Thank you!")