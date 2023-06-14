# Shopping cart program

foods = []
prices = []
total = []

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = int(input(f"enter the price of a {food} \u20B9" ))
        foods.append(food)
        prices.append(price)

print()
print("-------YOUR CART-------")

for food in foods:
    print(food, end=", ")

total = 0

for price in prices:
    total = total + price

print((f"\nYour Total is= \u20B9{total}"))

