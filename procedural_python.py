def food_bill_total(bill):
    total = 0.00
    for k, v in bill.items():
        total += v
    return total


def calculate_tax(percent, bill_total):
    return round((percent*bill_total) / 100.0, 2)


Food_bill = {
    1: 3.99,
    2: 4.55,
    3: 11.99,
    4: 22.00,
    5: 2.00
}


food_price = food_bill_total(Food_bill)
tax = calculate_tax(15, food_price)
print("Final Bill: ", food_price + tax, " USD")
