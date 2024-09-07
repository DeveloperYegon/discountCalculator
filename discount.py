
def calculate_discount(price, discount_percent):
    if (discount_percent>20):
        discount=price * discount_percent / 100
        return price - discount
    else:
        return price
price=int(input("Enter the price: "))
discount_percent=int(input("Enter the discount percentage: "))

print("The final price after discount is: ",calculate_discount(price,discount_percent))