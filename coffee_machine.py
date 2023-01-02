class CoffeeMachine:
    # initial resources
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    # remains
    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "ml of water")
        print(self.milk, "of milk")
        print(self.beans, "g of coffee beans")
        print(self.cups, "disposable cups")
        currency = "${:}".format(self.money)
        print(currency, "of money")

    # fill the coffee machine
    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: "))

    # make espresso
    def espresso(self):
        if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
            print("I have enough resources, making you a coffee!")
        else:
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")

    # make latte
    def latte(self):
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
            print("I have enough resources, making you a coffee!")
        else:
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")

    # make cappuccino
    def cappuccino(self):
        if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
            print("I have enough resources, making you a coffee!")
        else:
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")

    # buy coffee
    def buy(self):
        response = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if response == "back":
            pass
        elif response == "1":
            self.espresso()
        elif response == "2":
            self.latte()
        elif response == "3":
            self.cappuccino()

    # take money
    def take(self):
        currency = "${:}".format(self.money)
        print("I gave you", currency)
        self.money = 0

    # choose an option
    def actions(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit): ")
            if action == "remaining":
                self.remaining()
            elif action == "fill":
                self.fill()
            elif action == "buy":
                self.buy()
            elif action == "exit":
                break
            elif action == "take":
                self.take()
# initilaze
machine = CoffeeMachine()
machine.actions()
