cost = int(1000)
discount = int(20)
quantity = int(3)

total_cost = float((cost - ((cost * 20) / 100)) * quantity)

print(f"Стоимость вашего заказа: {total_cost} рублей")
