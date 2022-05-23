# purpose:  a software system to keep track of stock items and prices
# group: CP01/04
# author: Yazeed Abu-Hummos
# UWE ID: 21014295
# last edit time and date: 23:57 13/01/2022


class StockItem():
    category = "Car accessories"

    def __init__(self, code="", quantity=0, price=0.0):
        self.__code = code
        self.__quantity = quantity
        self.__price = price

# setters
    def setCode(self, code):
        self.__code = code

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def setPrice(self, price):
        self.__code = price

# getters
    def getCode(self):
        return self.__code

    def getQuantity(self):
        return self.__quantity

    def getPrice(self):
        return self.__price

    def getPriceWithVat(self):
        return self.__price+(self.__price*(self.getVat()/100))

    def getStockName(self):
        return "Unknown Stock Name"

    def getStockDescription(self):
        return "Unkown Stock Description"

    def getVat(self):
        return 17.5

# methods
    def addStock(self, incAmount):
        if incAmount < 1:
            print("\n\n**Error: Increment amount should be greter than 1**")
        elif incAmount+self.__quantity > 100:
            print("\n\n**Error: Stock can't be more than 100**")
        else:
            print("\n\n**Item %s: Increasing %d more units**" %
                  (self.getCode(), incAmount))
            self.__quantity += incAmount

    def sellStock(self, decAmount):
        if (decAmount < 1):
            print(
                "\n\n**Error: Decremenent amount should be greater than or equal to 1**")
        elif (decAmount <= self.__quantity):
            print("\n\n**Item %s: Sold %d units**" %
                  (self.getCode(), decAmount))
            self.__quantity -= decAmount
        else:
            print("\n\n**Error: Decremenent amount can't be greater than quantity**")

    def changePrice(self, newPrice):
        if newPrice >= 1:
            print("\n\n**Item %s: Price changed from %.2f " %
                  (self.getCode(), self.__price), end="")
            self.__price = newPrice
            print("to %.2f**" % self.__price)
        else:
            print(
                "\n\n**Error: New price should be greater than or equal to 1**")

    def __str__(self):
        return ("""
Stock Category: %s
Stock Type: %s
Description: %s
StockCode: %s
PriceWithoutVAT: £%.2f
PriceWithVAT: £%.2f
Total Unit in stock: %d unit
""" % (self.category, self.getStockName(), self.getStockDescription(), self.getCode(), self.getPrice(), self.getPriceWithVat(), self.getQuantity()))


class NavSys(StockItem):
    def __init__(self, code="", quantity=0, price=0.0, brand=""):
        super().__init__(code, quantity, price)
        self.__brand = brand

# setters
    def setBrand(self, brand):
        self.__brand = brand

# getters
    def getBrand(self):
        return self.__brand

    def getStockName(self):
        return "Navigation system"

    def getStockDescription(self):
        return "GeoVision Sat Nav"

    def __str__(self):
        return super().__str__()+"Brand: %s\n" % self.getBrand()


class Tire(StockItem):
    def __init__(self, code="", quantity=0, price=0.0, identification=""):
        super().__init__(code, quantity, price)
        self.__identification = identification

# setters
    def setIdentification(self, identification):
        self.__identification = identification

# getters
    def getIdentification(self):
        return self.__identification

    def getStockName(self):
        return "Pneumatic Tire"

    def getStockDescription(self):
        return "Air filled rubber tires mounted aroud wheels"

    def __str__(self):
        return super().__str__()+"identification: %s\n" % self.getIdentification()


class MountedHolder(StockItem):
    def __init__(self, code="", quantity=0, price=0.0, material="", magnetic="yes"):
        super().__init__(code, quantity, price)
        self.__material = material
        self.__magnetic = magnetic

# setters
    def setMaterial(self, material):
        self.__material = material

    def set_magnetic(self, magnetic):
        self.__magnetic = magnetic

# getters
    def getMaterial(self):
        return self.__material

    def getMagnetic(self):
        return self.__magnetic

    def getStockName(self):
        return "Car Mounted Holder"

    def getStockDescription(self):
        return "Holds your phone against windshield or air vents"

    def __str__(self):
        return super().__str__()+"Material made of: %s\n" % self.getMaterial()+"Is magnetic: %s\n" % self.getMagnetic()


class FogLight(StockItem):
    def __init__(self, code="", quantity=0, price=0.0, power=0):
        super().__init__(code, quantity, price)
        self.__power = power

# setters
    def setPower(self, power):
        self.__power = power

# getters
    def getPower(self):
        return self.__power

    def getStockName(self):
        return "Fog lights"

    def getStockDescription(self):
        return "Increases visibility in foggy weather"

    def __str__(self):
        return super().__str__()+"Power: %s Watts\n " % self.getPower()


if __name__ == "__main__":
    # StockItem testing cases
    si = StockItem("SI101", 20, 99.99)
    print(si)
    si.addStock(200)
    si.addStock(-5)
    si.addStock(5)
    print(si)
    si.sellStock(300)
    si.sellStock(0)
    si.sellStock(10)
    print(si)
    si.changePrice(150)
    si.changePrice(-5)
    print(si)

    # NavSys testing cases
    ns = NavSys("NS101", 10, 299.99, "TomTom")
    print(ns)
    ns.addStock(101)
    ns.addStock(0)
    ns.addStock(100)
    print(ns)
    ns.sellStock(120)
    ns.sellStock(-5)
    ns.sellStock(110)
    print(ns)
    ns.changePrice(199.99)
    print(ns)

    # Tire testing cases
    t = Tire("T101", 25, 250, "P205/65R16")
    print(t)
    t.sellStock(300)
    t.sellStock(50)
    t.sellStock(10)
    print(t)
    t.addStock(200)
    t.addStock(-5)
    t.addStock(5)
    print(t)
    t.changePrice(150)
    print(t)

    # MountedHolder testing cases
    mh = MountedHolder("MH101", 50, 9.99, "Plastic", "no")
    print(mh)
    mh.changePrice(20)
    mh.addStock(200)
    mh.addStock(-5)
    mh.addStock(5)
    print(mh)
    mh.sellStock(300)
    mh.sellStock(0)
    mh.sellStock(10)
    print(mh)
    mh.changePrice(8.79)
    print(mh)

    # FogLight testing cases
    fl = FogLight("FL101", 10, 12.49, 220)
    print(fl)
    fl.addStock(5)
    fl.sellStock(10)
    fl.addStock(15)
    fl.sellStock(-2)
    fl.addStock(200)
    print(fl)
    fl.changePrice(1.50)
    print(fl)
