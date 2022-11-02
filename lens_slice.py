toppings=["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2,6,1,3,2,7,2]

num_two_dollar_slices = prices.count(2)
num_pizzas=len(toppings)

print(f'We sell {num_pizzas} different kinds of pizza!')

pizza_and_prices = list(zip(prices,toppings))
sorted_pizza_and_prices=sorted(pizza_and_prices)

cheapest_pizza= sorted_pizza_and_prices[0]
#print(cheapest_pizza)
priciest_pizza = sorted_pizza_and_prices[-1]
#print(priciest_pizza)
sorted_pizza_and_prices.pop()
#print(sorted_pizza_and_prices)
sorted_pizza_and_prices.insert(4,[2.5, "peppers"])
#print(sorted_pizza_and_prices)

three_cheapest=sorted_pizza_and_prices[:3]
print(three_cheapest)