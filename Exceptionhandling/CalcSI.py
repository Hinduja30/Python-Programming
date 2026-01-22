print("connection to server")
try:
    p = int(input("Enter the principal amount"))
    t = int(input("Enter the period of time"))
    r = float(input("Enter the rate "))
    SI = (p*t*r)/100
    print("simple Interest ",SI)

except ValueError as e:
    print("Incorrect type of value" , e )

finally:
    print("connection closed")
