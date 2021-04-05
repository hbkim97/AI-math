class FruitSeller:
    def __init__(self, money, appleNum, price):
        self.mymoney = money
        self.numOfApple = appleNum
        self.APPLE_PRICE = price

    def saleApple(self, money):
        num = money / self.APPLE_PRICE[0]
        self.numOfApple -= num
        self.myMoney += money
        return num

    def showSaleResult(self):
        print("남은 사과는:" + str(self.numOfApple))
        print("판매 매출은:" + str(self.myMoney))

class FruitBuyer:
    def __init__(self, money, appleNum):
        self.myMoney = money
        self.numOfApple = appleNum

    def buyApple(self, seller, money):
        self.numOfApple += seller.saleApple(money)
        self.myMoney -= money

    def showBuyResult(self):
        print("구매한 사과는:" + str(self.numOfApple))
        print("남은 돈은:" + str(self.myMoney))

seller1 = FruitSeller(1000,20, 1000)
seller2 = FruitSeller(2000,30, 1500)
seller3 = FruitSeller(0, 100, 800)

buyer1 = FruitBuyer(1000,5)
buyer2 = FruitBuyer(5000,8)
buyer3 = FruitBuyer(1000000,5000)

buyer2.buyApple()