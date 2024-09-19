'''''
# Function to calculate profit or loss
def calculate_profit_or_loss(cost_price, selling_price):
    # Cost price for one banana
    cost_per_banana = cost_price / 12
    # Total selling price for a dozen bananas
    total_selling_price = selling_price * 12
    
    # Calculate profit or loss
    profit_or_loss = total_selling_price - cost_price
    return profit_or_loss

# Input
cost_price = float(input("Enter the total cost of a dozen bananas (X): "))
selling_price = float(input("Enter the selling price of one banana (Y): "))

# Calculate and print profit or loss
result = calculate_profit_or_loss(cost_price, selling_price)

if result > 0:
    print(f"Profit: Rs.{result:.2f}")
elif result < 0:
    print(f"Loss: Rs.{-result:.2f}")
else:
    print("No profit, no loss.")
