
print("Welcome to the logistics cost calculator page! We will calculate for you three options:")
weight = int(input("Please enter the weight: "))

if weight <= 2:
  cost_ground= weight*1.50+20.00
elif 6 >= weight > 2:
  cost_ground = weight*3.00 +20.00
elif 10 >= weight > 6:
  cost_ground =weight*4.00 + 20.00
else:
  cost_ground= weight*4.75 + 20.00

#print(cost_ground)
#Premium ground shipping
premium_cost_ground = 125.00
#print(premium_cost_ground)
#Drone shipping
if weight <=2:
  cost_dron = weight*4.50
elif 6 >= weight >2:
  cost_dron = weight*9.00
elif 10 >= weight >6:
  cost_dron = weight*12.00
else:
  cost_dron = weight*14.25
#print(cost_dron)



print("For",weight,"kg the cost of: ")
print("Ground shipping is",cost_ground, "USD")
print("Premium ground shipping is",premium_cost_ground, "USD")
print("Drone shipping is",cost_dron, "USD")
