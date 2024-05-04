price = input('Enter price of goods:')
price = int(price)

discount = 0.2*price

if price >= 5000 :
    newprice =  price-discount
    print('Your discount is ',discount,'You should pay ',newprice)
else:
    print('You are not eligible for discount, pay ',price)



