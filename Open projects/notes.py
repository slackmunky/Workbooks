# Austin Chronicle elements to find music listings at
# https://www.austinchronicle.com/events/music/YYYY-MM-DD/
# body >
#       div#total-containment >
#       div#content-area.clear-fix >
#       div#cal-left >
#       section#listings
# Relevant data start on line 3371 and ends on 4518
# Need to figure out how to compare current foreign data to
# current local data and only pull changes


# Basic class and method
class Rules():
    def washing_brushes(self):
        print("Point bristles towards the basin while washing your brushes.")


# Gives "chore" a rules class
chore = Rules()
# Calls the method attached to the class
chore.washing_brushes()


# Class and method with argument
class CircleArea():
    # Define a class object
    pi = 3.14

    def area(self, radius):
        # "self.pi" calls the class object into the method
        print("Area is: " + str(self.pi * radius ** 2))


# Gives variable object a class
circle = CircleArea()

# circle.area calls "area" method of "Circle()" with radius argument
teaching_table_area = circle.area(36 / 2)


# Class with constructor(__init__)
class CircleInfo:
    pi = 3.14

    # "__init__" performs method whenever class is called
    def __init__(self, diameter):
        print("New circle with diameter: {diameter}".format(
                diameter=diameter
        ))


teaching_table = CircleInfo(36)  # performs class constructor method


# Another class with constructor
class Shout:
    def __init__(self, phrase):
        if type(phrase) == str:
            print(phrase.upper())


shouter = Shout("I'm not listening!")


# ".store_name" (or whatever descriptor you want) adds instanced
# attributes to objects to be called on later
class Store:
    # Does nothing, used when a statement is needed syntactically
    pass


# Gives objects a class
alternative_rocks = Store()
isabelles_ices = Store()

# Assigns instanced attributes with whatever name you choose.
# Could be "alternative_rocks.asldkhg"
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

store_string = "{} {}".format(
        alternative_rocks.store_name,
        isabelles_ices.store_name)
print(store_string)


class NoCustomAttributes:
    pass


attributeless = NoCustomAttributes()

try:
    attributeless.fake_attribute
except AttributeError:
    # This is printed as the instanced attribute is not yet assigned
    print("This text gets printed!")

attributeless.fake_attribute = "Not attributeless anymore."
# Prints "Not attributeless anymore." because that's true now
print(attributeless.fake_attribute)

# Checking if an object has an attribute and
# returning a value using the attribute checked for
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for entry in how_many_s:
    if hasattr(entry, "count") != True:
        continue
    else:
        print(entry.count("s"))


class SearchEngineEntry:
    secure_prefix = "https://"

    # Adds argument of SearchEngineEntry("argument") as
    # definition of url attribute for object
    def __init__(self, url):
        self.url = url

    # object_name.secure() adds "https://" for secure
    # connection to previously created url
    def secure(self):
        return "{prefix}{site}".format(prefix=self.secure_prefix,
                                       site=self.url)


# Defines url instance attribute
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
print(codecademy.url)
print(wikipedia.url)
# Adds secure prefix to url instance attribute and prints
print(codecademy.secure())
print(wikipedia.secure())


class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))

        self.radius = diameter / 2

    def circumference(self):
        circumference = 2 * self.pi * self.radius
        return circumference


medium_pizza = Circle(12)
print("Circumference is {c}".format(c=medium_pizza.circumference()))
teaching_table = Circle(36)
print("Circumference is {c}".format(c=teaching_table.circumference()))
round_room = Circle(11460)
print("Circumference is {c}".format(c=round_room.circumference()))


# Creating a subclass
class Bin:
    pass


# Lists "Bin" as the superclass for the TrashBin subclass
class TrashBin(Bin):
    pass


# Defines OutOfStock as a subclass of native Exception class
class OutOfStock(Exception):
    pass


# Set up for testing OutOfStock Exception
class CandleShop:
    # Not particularly important, funny, or clever
    name = "Here's a Hot Tip: Buy Drip Candles"

    # Adds ability to add stock
    def __init__(self, stock):
        self.stock = stock

    # Adds ability to deplete stock
    def buy(self, color):
        # This is what raises the error
        if self.stock[color] < 1:
            raise OutOfStock
        # subtracts from stock
        self.stock[color] = self.stock[color] - 1


# initial stock
candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
# This does not raise an exception
candle_shop.buy('blue')


# candle_shop.buy('green')
# This ^ raises the OutOfStock exception because there are no green candles

# Setup for overriding method using classes
class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text


# Defines user traits
class User:
    def __init__(self, username):
        self.username = username

    def edit_message(self, message, new_text):
        # checks if the user attempting to edit is the one who wrote it
        if message.sender == self.username:
            message.text = new_text


class Admin(User):
    # Bypasses the user check if the user is an Admin
    def edit_message(self, message, new_text):
        message.text = new_text


# Inheriting from parent class using super() as temp object
class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions


class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        # Inherits traits from superclass
        super().__init__(potatoes, celery, onions)
        # Adds raisins, because gross
        self.raisins = 40
