class PriceItem:

    def __init__(self,code,name,kkal,price):
        self.__code = code
        self.__name = name
        self.__kkal = kkal
        self.__price = price

    def checkItem(self,code):
        if self.__code == code:
            return True
        else:
            return False

    def getCode(self):
        return self.__code

    def getName(self):
        return self.__name

    def getKkal(self):
        return self.__kkal

    def getPrice(self):
        return self.__price
