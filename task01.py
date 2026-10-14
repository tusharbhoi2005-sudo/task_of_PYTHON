# 1. Calculate Electronics GST (18%)
def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst


# 2. Calculate Fashion GST (13%)
def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst


# 3. Calculate Food GST (7%)
def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


# 4. Calculate Total Bill after GST
def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


# 5. Calculate Discounted Bill (20% discount)
def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100

    return total - discount


# Main Program
a = 100
b = 100
c = 100
d = 100
e = 100

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100

final_amount = calculateDiscountedBill(a, b, c, d, e)

print(f"Total after GST = {total:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Final payable amount = {final_amount:.2f}")