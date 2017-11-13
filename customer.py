class Customer:

    def __init__(self, name):
        self.__name = name
        self.__credit_card_num = ''
        self.__credit_security_code = ''
        self.__debit_card_num = ''
        self.__debit_pin = ''

    def inputCardsInfo(self):
        credit_card_num=input('Enter credit card number: ')
        self.__credit_card_num = credit_card_num
        credit_security_code = input('Enter 3-digit security code: ')
        while len(credit_security_code) != 3 or not credit_security_code.isdigit():
            print('Invalid security code')
            credit_security_code = input('Enter 3-digit security code: ')
        self.__credit_security_code = credit_security_code
        debit_card_num = input('Enter debit card number: ')
        self.__debit_card_num = debit_card_num
        debit_pin = input('Enter 4-digit PIN: ')
        while len(debit_pin) != 4 or not debit_pin.isdigit():
            print('Invalid pin type')
            debit_pin = input('Enter 4-digit PIN: ')
        self.__debit_pin = debit_pin

    def verifyCreditCard(self,security_code):
        if self.__credit_security_code == security_code:
            return True
        else:
            return False

    def verifyDebitCard(self,pin):
        if self.__debit_pin == pin:
            return True
        else:
            return False

    def creditCardLastFour(self):
        return self.__credit_card_num[-4:]

    def debitCardLastFour(self):
        return self.__debit_card_num[-4:]
