from inventary.add_product import add_product
from billing.calculate_bills import calculate_bills
from utilities.logging import logging

logging("Application startted")
add_product("laptop",10)
cart=[
    {'name':'Laptop','price':100000,'quantity':2},
    {'name':'Mouse','price':250,'quantity':5}
]
total = calculate_bills(cart)
logging(f"the total bill is:{total}")