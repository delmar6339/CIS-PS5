principle = float(input("Enter the principle amount: "))
years_to_maturity = int(input("Enter the years to maturity: "))
if principle > 100000 and years_to_maturity == 5:
    interest_rate = 0.06
elif 50000 <= principle <= 100000 and years_to_maturity == 10:
    interest_rate = 0.05
elif 50000 <= principle <= 100000 and years_to_maturity == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02
first_year_interest = principle * interest_rate
print(f"Principle: ${principle:.2f}")
print(f"Interest Rate: {interest_rate*100:.2f}%")
print(f"First Year Interest: ${first_year_interest:.2f}")