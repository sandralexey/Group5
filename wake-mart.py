from customer import Customer

def scanPrices(price_list):
    total_price = 0.0
    item = input('Enter 4-digit item code [or 9999 to stop]: ')
    while item != '9999':
        if item in price_list:
            price = price_list[item]
            print('Item found. Price:',price)
            total_price = total_price + price
        else:
            print('Item not found')
        item = input('Enter 4-digit item code [or 9999 to stop]: ')
    print('Total price:',total_price)
    print()
    return total_price

def scanCoupons(coupon_list):
    total_coupons = 0.0
    item = input('Enter 4-digit coupon code [or 9999 to stop]: ')
    while item != '9999':
        if item in coupon_list:
            coupon = coupon_list[item]
            print('Coupon found. Value:',coupon)
            total_coupons = total_coupons + coupon
        else:
            print('Coupon not found')
        item = input('Enter 4-digit coupon code [or 9999 to stop]: ')
    print('Total coupon value:',total_coupons)
    print()
    return total_coupons

def readPriceList():
    price_list = dict()
    price_file = open('price_list.txt','r')
    for line in price_file:
        line = line.strip()
        price = line.split( )
        price_list[price[0]] = float(price[1])
    price_file.close()
    print('Price list:')
    price_list_touples = price_list.items()
    for tup in price_list_touples:
        print(tup)
    print()
    return price_list

def readCouponList():
    coupon_list = dict()
    coupon_file = open('coupon_list.txt','r')
    for line in coupon_file:
        line = line.strip()
        coupon = line.split( )
        coupon_list[coupon[0]] = float(coupon[1])
    coupon_file.close()
    print('Coupon list:')
    coupon_list_touples = coupon_list.items()
    for tup in coupon_list_touples:
        print(tup)
    print()
    return coupon_list

def makePayment(customer,total_amount):
    successful_payment = False
    while successful_payment == False:
        print('Please choose payment method.')
        payment_type = input('Please enter 1 for credit card, 2 for debit card: ')
        while payment_type != '1' and payment_type != '2':
            print('INVALID INPUT - payment_type should be 1 or 2')
            payment_type = input('Please enter 1 for credit card, 2 for debit card: ')
        if payment_type == '1':
            credit_security_code = input('Please enter 3-digit security code: ')
            while len(credit_security_code) != 3 or not credit_security_code.isdigit():
                print('Invalid security code')
                credit_security_code = input('Enter 3-digit security code: ')
            if customer.verifyCreditCard(credit_security_code):
                print('The amount of', total_amount, 'will be charged to card number ending with',customer.creditCardLastFour())
                successful_payment = True
        else:
            debit_pin = input('Please enter 4-digit PIN:')
            while len(debit_pin) != 4 or not debit_pin.isdigit():
                print('Invalid pin type')
                debit_pin = input('Enter 4-digit PIN: ')
            if customer.verifyDebitCard(debit_pin):
                print('The amount of', total_amount, 'will be charged to card number ending with',customer.debitCardLastFour())
                successful_payment = True

def main():

    print('Welcome to Wake-Mart. Please register.')
    name = input('Enter your name: ')
    customer1=Customer(name)
    customer1.inputCardsInfo()
    print('Registration completed')
    print()
    price_list=readPriceList()
    total_price = scanPrices(price_list)
    coupon_list = readCouponList()
    total_coupons = scanCoupons(coupon_list)
    total_amount = total_price - total_coupons
    print('Please pay this amount:',total_amount)
    print()
    makePayment(customer1,total_amount)

main()
