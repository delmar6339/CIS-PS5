quantity = int(input("Enter the quantity of widgets: "))
if quantity > 10000:
    price = 10
elif quantity > 5000:
    price = 20
else:
    price = 30
extended_price = quantity * price
tax_amount = 0.07 * extended_price
total = extended_price + tax_amount
print(f"Extended Price: ${extended_price:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")