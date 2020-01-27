# Basic class and method
class Rules():
    def washing_brushes(self):
        print("Point bristles towards the basin while washing your brushes.")


chore = Rules()  # Gives "chore" a rules class
chore.washing_brushes()  # Calls the method attached to the class


# Class and method with argument
class CircleArea():
    pi = 3.14  # Define a class object

    def area(self, radius):
        print("Area is: " + str(self.pi * radius ** 2))  # "self.pi" calls the class object into the method


circle = CircleArea()  # Gives object a class

teaching_table_area = circle.area(
    36 / 2)  # circle.area calls the "area" method of the "Circle()" class with radius argument


# Class with constructor(__init__)
class CircleInfo:
    pi = 3.14

    def __init__(self, diameter):  # "__init__" performs method whenever class is called
        print("New circle with diameter: {diameter}".format(diameter=diameter))


teaching_table = CircleInfo(36)  # performs class constructor method


# Another class with constructor
class Shout:
    def __init__(self, phrase):
        if type(phrase) == str:
            print(phrase.upper())


shouter = Shout("I'm not listening!")


# ".store_name" (or whatever descriptor you want) adds instanced attributes to objects to be called on later
class Store:
    pass  # Does nothing, I guess


# Gives objects a class
alternative_rocks = Store()
isabelles_ices = Store()

# Assigns instanced attributes with whatever name you choose. Could be "alternative_rocks.asldkhg"
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

store_string = "{} {}".format(alternative_rocks.store_name, isabelles_ices.store_name)
print(store_string)


class NoCustomAttributes:
    pass


attributeless = NoCustomAttributes()

try:
    attributeless.fake_attribute
except AttributeError:
    print("This text gets printed!")  # This is printed as the instanced attribute is not yet assigned

attributeless.fake_attribute = "Not attributeless anymore."
print(attributeless.fake_attribute)  # Prints "Not attributeless anymore." because that's true now

# Checking if an object has an attribute and returning a value using the attribute checked for
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for entry in how_many_s:
    if hasattr(entry, "count") != True:
        continue
    else:
        print(entry.count("s"))


class SearchEngineEntry:
    secure_prefix = "https://"

    # Adds argument of SearchEngineEntry("argument") as definition of url attribute for object
    def __init__(self, url):
        self.url = url

    # object_name.secure() adds "https://" for secure connection to previously created url
    def secure(self):
        return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)


codecademy = SearchEngineEntry("www.codecademy.com")  # Defines url instance attribute
wikipedia = SearchEngineEntry("www.wikipedia.org")
print(codecademy.secure())  # Adds secure prefix to url instance attribute and prints
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

