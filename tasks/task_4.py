price: int = int(50)
quantity: int = 3
total_cost: int = price * quantity

print(
    f"Вы должны заплатить {total_cost} рублей за {quantity} едениц "
    f"товара по цене {price} рублей за еденицу"
)
