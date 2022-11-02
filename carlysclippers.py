hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#find average price
total_price = 0
for price in prices:
    total_price+=price
average_price = total_price/len(prices)
print(f"Average Haircut Price: {average_price}")

# cut prices by 5 dollars
new_prices = [price-5 for price in prices]
print(new_prices)

#find last weeks revenue
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i]*last_week[i]
print(f"Total Revenue: {total_revenue}")

#find average daily revenue
average_daily_revenue = total_revenue/7
print(average_daily_revenue)

cuts_under_30 = [price for price in new_prices if price < 30]
print(cuts_under_30)