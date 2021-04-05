class FruitSeller:
    numOfApple = 20
    myMoney = 0
    APPLE_PRICE = (1000,0)

    def saleApple(self,money):
        num = money / self.APPLE_PRICE[0]
        self.numOfApple -= num
        self.myMoney += money
        return num

    def showSaleResult(self):
        print("남은 사과는:" + str(self.numOfApple))
        print("판매 매출은:" + str(self.myMoney))

class FruitBuyer:
    numOfApple = 0
    myMoney = 5000

    def buyApple(self,seller,money):
        self.numOfApple += seller.saleApple(money)
        self.myMoney -= money

    def showBuyResult(self):
        print("구매한 사과는:" + str(self.numOfApple))
        print("남은 돈은:" + str(self.myMoney))

heeseok = FruitSeller()
bravegirls = FruitBuyer()

bravegirls.buyApple(heeseok, 2000)

heeseok.showSaleResult()
bravegirls.showBuyResult()
