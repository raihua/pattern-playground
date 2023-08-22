from abc import ABC, abstractmethod

'''
Abstract factory is a creational design pattern that lets you create factories of objects without specifying concrete classes.
A way to understand this is that we have classes for the variant of the product we want. Based on that variant, we are able
create different kinds of products. For example, toys. Toy abstract class has sub classes: ElectricToy, WoodToy. These would
override methods like makeBearToy(), makeSoldierToy()
'''

class BookingManager:
    def __init__(self):
        pass

    def createBooking(self):
        pass
        # call pricing policy


class IPricingPolicy(ABC):
    @abstractmethod
    def getTotalPrice(self, basePrice):
        pass

class PercentDiscountPricingPolicy(IPricingPolicy):
    def __init__(self, percentDiscount):
        self.percentDiscount = percentDiscount

    def getTotalPrice(self, basePrice):
        totalPrice = "TotalPrice"
        return totalPrice
    

class DollarDiscountPricingPolicy(IPricingPolicy):
    def __init__(self, dollarDiscount):
        self.dollarDiscount = dollarDiscount

    def getTotalPrice(self, basePrice):
        totalPrice = "TotalPrice"
        return totalPrice
    

class FullPricetPricingPolicy(IPricingPolicy):
    def __init__(self, fullPriceDiscount):
        self.fullPriceDiscount = fullPriceDiscount

    def getTotalPrice(self, fullPriceDiscount):
        totalPrice = fullPriceDiscount
        return totalPrice
