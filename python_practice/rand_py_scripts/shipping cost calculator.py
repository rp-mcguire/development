weight = 4.8

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 +20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 +20
print("Ground Shipping cost $", cost_ground)

premium_ground_cost = 125
print("Premium Ground Shipping cost $", premium_ground_cost)

#Drone Shipping
if weight <= 2:
  drone_cost = weight * 4.5
elif weight > 2 and weight <= 6:
  drone_cost = weight * 9
elif weight > 6 and weight <= 10:
  drone_cost = weight * 12
else:
  drone_cost = weight * 14.25
print("Drone Shipping cost $", drone_cost)
