class Rules():
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."


class Circle():
    pi = 3.14

    def area(self, radius):
        return self.pi * radius ** 2


circle = Circle()

pizza_area = circle.area(.5 * 12)
print(pizza_area)


