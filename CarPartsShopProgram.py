# purpose:  a software system to keep track of stock items and prices
# group: CP01/04
# author: Yazeed Abu-Hummos
# UWE ID: 21014295
# last edit time and date: 23:57 13/01/2022


import os
from CarPartsShopClasses import *
lists = {"stockitem": [],
         "navsys": [],
         "tire": [],
         "mountedholder": [],
         "foglight": []}
canLoad = True


def codeValidation():
    try:
        code = input("Enter item's code: ").lower()
    except ValueError:
        print("Invalid code, try again")
        code = codeValidation()
    try:
        if code in lists:
            print("Code already used as a stock type")
            code = codeValidation()
        if typeCodeChecker(code).getCode() == code:
            print("Code already used")
            code = codeValidation()
    except AttributeError:
        pass
    return code


def valueValidation(valueType):
    try:
        if valueType == "price":
            value = float(input("Enter item's %s: " % valueType))
        elif valueType == "quantity" or valueType == "power":
            value = float(input("Enter item's %s: " % valueType))
        elif valueType == "magnetic":
            value = input("Is the item magnetic [yes/no]: ").lower()
            while value not in ["yes", "no"]:
                value = input(
                    "Invalid input, try again\nIs the item magnetic [yes/no]: ").lower()
        else:
            value = input("Enter item's %s: " % valueType).lower()
    except ValueError:
        print("Invalid %s, try again" % valueType)
        value = valueValidation(valueType)
    if type(value) != str and value < 1:
        print("%s out of range, try again" % valueType)
        value = valueValidation(valueType)
    if valueType == "quantity" and value > 100:
        print("%s out of range, try again" % valueType)
    return value


def typeCodeChecker(userCode):
    for typeList in lists:
        for item in lists[typeList]:
            if item.getCode() == userCode:
                return item
    else:
        return "\n\n**Item not found**"


def guide():
    print("""+--------------------------------------------------------------------------------------------------------------------+
|                                                                                                                    |
|       ______                        ____                      __                         __                        |
|      / ____/  ____ _   _____       / __ \   ____ _   _____   / /_   _____       _____   / /_     ____     ____     |
|     / /      / __ `/  / ___/      / /_/ /  / __ `/  / ___/  / __/  / ___/      / ___/  / __ \   / __ \   / __ \    |
|    / /___   / /_/ /  / /         / ____/  / /_/ /  / /     / /_   (__  )      (__  )  / / / /  / /_/ /  / /_/ /    |
|    \____/   \__,_/  /_/         /_/       \__,_/  /_/      \__/  /____/      /____/  /_/ /_/   \____/  / .___/     |
|                                                                                                       /_/          |
|                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------+
programme by: Yazeed Abu-Hummos (21014295)
______________________________________________________________________________________________________________________

-exit: closes the application
    --note that you can't exit while in action
    -- note that all unsaved data will be lost upon exiting
-create: creates a new item
-display: display's the information for that item
    --"all" will display everything
    --*stock type name* will display all items of that stock type
-add stock: adds stock
-sell stock: sells stock
-change price: changes price
-save: saves your stock
-load: loads your stock from a text file
    --note that you can not load data after crating an item or loading data (to avoid duplicate item codes)
-delete: deletes an item for you:
    --note that a deleted item can not be retrieved unless it was saved previously


-note that the programme is not case sensitive
______________________________________________________________________________________________________________________

""")
    for listType in lists:
        if len(lists[listType]) == 0:
            print(listType+":", end="\n")
        else:
            print(listType+": ", end="")
            for item in lists[listType]:
                if item == lists[listType][-1]:
                    print(item.getCode())
                else:
                    print(item.getCode(), end=" / ")
    print("\n\n")


guide()
userInput = input("What would you like to do: ").lower()

os.system("cls")
while True:
    guide()
    if userInput == "exit":
        break

    elif userInput == "create":
        print("**Creating item**\n\n")
        while userInput not in lists:
            userInput = input(
                "What type of item are you adding (choose from list shown above): ").lower()
        if userInput == "navsys":
            lists[userInput].append(
                NavSys(codeValidation(), valueValidation("quantity"), valueValidation("price"), valueValidation("brand")))
        elif userInput == "tire":
            lists[userInput].append(
                Tire(codeValidation(), valueValidation("quantity"), valueValidation("price"), valueValidation("identification")))
        elif userInput == "mountedholder":
            lists[userInput].append(
                MountedHolder(codeValidation(), valueValidation("quantity"), valueValidation("price"), valueValidation("material"), valueValidation("magnetic")))
        elif userInput == "foglight":
            lists[userInput].append(
                FogLight(codeValidation(), valueValidation("quantity"), valueValidation("price"), valueValidation("power")))
        else:
            lists[userInput].append(
                StockItem(codeValidation(), valueValidation("quantity"), valueValidation("price"),))
        print("\n\n**Item created**")
        canLoad = False

    elif userInput == "display":
        print("**Disaplaying item(s)**\n\n")
        userInput = input("What is the code for the item: ").lower()
        if userInput == "all":
            for typeList in lists:
                for item in lists[typeList]:
                    print(item)
        elif userInput in lists:
            for item in lists[userInput]:
                print(item)
        else:
            print(typeCodeChecker(userInput))

    elif userInput == "change price":
        print("**Changing price**\n\n")
        userInput = input(
            "What is the code for the item you want to change it's price: ").lower()
        try:
            typeCodeChecker(userInput).changePrice(
                float(input("What is the new price: ")))
        except AttributeError:
            print("Error: Item not fount, unable to change price")
        except ValueError:
            print("Error: Invalid input, unable to change price")

    elif userInput == "add stock":
        print("**Adding stock**\n\n")
        userInput = input(
            "What is the code for the item you want to add stock to it: ").lower()
        try:
            typeCodeChecker(userInput).addStock(
                int(input("How much stock do you want to add: ")))
        except AttributeError:
            print("Error: Item not fount, unable to add stock")
        except ValueError:
            print("Error: Invalid input, unable to add stock")

    elif userInput == "sell stock":
        print("**Selling stock**\n\n")
        userInput = input(
            "What is the code for the item you want to sell stock from it: ").lower()
        try:
            typeCodeChecker(userInput).sellStock(
                int(input("How much stock do you want to sell: ")))
        except AttributeError:
            print("Error: Item not fount, unable to sell stock")
        except ValueError:
            print("Error: Invalid input, unable to sell stock")

    elif userInput == "save":
        print("**Saving data**\n\n")
        for txtfile in os.listdir("savedData"):
            print(txtfile[:-4])
        userInput = input(
            "Chose the name of the file you want to save data to : ").lower()
        try:
            f = open("savedData/%s.txt" % userInput, "x")
        except FileExistsError:
            f = open("savedData/%s.txt" % userInput, "w")
        for listType in lists:
            for item in lists[listType]:
                if listType == "stockitem":
                    f.writelines("%s %s %d %.2f\n" % (
                        listType, item.getCode(), item.getQuantity(), item.getPrice()))
                elif listType == "navsys":
                    f.writelines("%s %s %d %.2f %s\n" % (
                        listType, item.getCode(), item.getQuantity(), item.getPrice(), item.getBrand()))
                elif listType == "tire":
                    f.writelines("%s %s %d %.2f %s\n" % (
                        listType, item.getCode(), item.getQuantity(), item.getPrice(), item.getIdentification()))
                elif listType == "mountedholder":
                    f.writelines("%s %s %d %.2f %s %s\n" % (
                        listType, item.getCode(), item.getQuantity(), item.getPrice(), item.getMaterial(), item.getMagnetic()))
                elif listType == "foglight":
                    f.writelines("%s %s %d %.2f %d\n" % (
                        listType, item.getCode(), item.getQuantity(), item.getPrice(), item.getPower()))
        f.close()
        print("\n\n**Data saved**")

    elif userInput == "load" and canLoad == True:
        print("**Loading data**\n\n")
        for txtfile in os.listdir("savedData"):
            print(txtfile[:-4])
        userInput = input(
            "Chose the name of the file you want to load data from: ").lower()
        try:
            f = open("savedData/%s.txt" % userInput, "r")
        except FileNotFoundError:
            print("\n\n**File not found**")
        else:
            for line in f.readlines():
                word = list(line.split())
                if word[0] == "stockitem":
                    lists["stockitem"].append(
                        StockItem(word[1], int(word[2]), float(word[3])))
                elif word[0] == "navsys":
                    lists["navsys"].append(
                        NavSys(word[1], int(word[2]), float(word[3]), word[4]))
                elif word[0] == "tire":
                    lists["tire"].append(
                        Tire(word[1], int(word[2]), float(word[3]), word[4]))
                elif word[0] == "mountedholder":
                    lists["mountedholder"].append(
                        MountedHolder(word[1], int(word[2]), float(word[3]), word[4], word[5]))
                elif word[0] == "foglight":
                    lists["foglight"].append(
                        FogLight(word[1], int(word[2]), float(word[3]), int(word[4])))
            f.close()
            print("\n\n**Data loaded**")
            canLoad = False

    elif userInput == "load" and canLoad == False:
        print("**You can't load items**\n\n")

    elif userInput == "delete":
        print("**Deleting item**\n\n")
        userInput = input(
            "What is the code for the item you want to delete: ").lower()
        for typeList in lists:
            try:
                lists[typeList].remove(typeCodeChecker(userInput))
                print("\n\n**Item deleted**")
                break
            except ValueError:
                continue
        else:
            print("\n\n**Item not found**")

    else:
        print("\n\n**Invalid keyword**")

    userInput = input("\n\nWhat would you like to do: ").lower()
    os.system("cls")
