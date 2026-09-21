def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number > 0:
                return number

            print("Value must be greater than zero.")

        except ValueError:
            print("Invalid value. Please enter a whole number.")


def get_positive_float(prompt):
    while True:
        try:
            number = float(input(prompt))

            if number > 0:
                return number

            print("Value must be greater than zero.")

        except ValueError:
            print("Invalid value. Please enter a number.")



item_name = input("Enter the item name: ")
quantity = get_positive_integer("Enter the required quantity: ")

print("\n--- Supplier 1 ---")
supplier_one_name = input("Enter supplier name: ")
supplier_one_price = get_positive_float("Enter unit price: $")

print("\n--- Supplier 2 ---")
supplier_two_name = input("Enter supplier name: ")
supplier_two_price = get_positive_float("Enter unit price: $")

supplier_one_total = quantity * supplier_one_price
supplier_two_total = quantity * supplier_two_price

print("\nProcureAI - Supplier Comparison")
print(f"Item: {item_name}")
print(f"Required quantity: {quantity}")

print(f"\n{supplier_one_name}")
print(f"Unit price: ${supplier_one_price:.2f}")
print(f"Total cost: ${supplier_one_total:.2f}")

print(f"\n{supplier_two_name}")
print(f"Unit price: ${supplier_two_price:.2f}")
print(f"Total cost: ${supplier_two_total:.2f}")

if supplier_one_total < supplier_two_total:
    savings = supplier_two_total - supplier_one_total
    print(f"\nRecommendation: Choose {supplier_one_name}.")
    print(f"Estimated savings: ${savings:.2f}")

elif supplier_two_total < supplier_one_total:
    savings = supplier_one_total - supplier_two_total
    print(f"\nRecommendation: Choose {supplier_two_name}.")
    print(f"Estimated savings: ${savings:.2f}")

else:
    print("\nRecommendation: Both suppliers have the same total cost.")