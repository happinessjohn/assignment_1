print("""
     This program takes in  two numbers and prints their sum, difference, product and quotient.
     """)
val1 = input("Enter the first value: ")
val2 = input("Enter the second: ")

sum_value = float(val1) + float(val2)

difference_value = float(val1) - float(val2)

product_value = float(val1) * float(val2)

quotient_value = float(val1) / float(val2)

print("\n\nResult:\n\n")

print(f"The sum of {str(val1)} and {str(val2)} is {str(sum_value)}\n\n")

print(f"The product of {str(val1)} and {str(val2)} is {str(product_value)}\n\n")

print(f"The difference between {str(val1)} and {str(val2)} is {str(difference_value)}\n\n")

print(f"The quotient value between {str(val1)} and {str(val2)} is {str(quotient_value)}\n\n")
