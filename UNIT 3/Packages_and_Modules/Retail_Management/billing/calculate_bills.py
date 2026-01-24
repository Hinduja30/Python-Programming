def calculate_bills(cart):
    total = sum(item['price'] * item['quantity'] for item in cart)
    return total