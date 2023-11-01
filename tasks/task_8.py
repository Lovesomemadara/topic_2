oklad: int = 50000
tax_rate: float = 0.13

tax: float = oklad * tax_rate
salary: float = oklad - tax

print(f"Размер зарплаты: {oklad} рублей")
print(f"Размер подоходного налога: {tax} рублей")
print(f"Сумма на руки: {salary} рублей")
