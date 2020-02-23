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


# Classes 17-ish through 245-ish
# Nodes 245-ish through 324-ish

# Basic class and method


class Rules:
    # noinspection PyMethodMayBeStatic
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."


# Gives "chore" a rules class
chore = Rules()
# Calls the method attached to the class
chore.washing_brushes()


# Class and method with argument
class CircleArea:
    # Define a class object
    pi = 3.14

    def area(self, radius):
        area = self.pi * radius ** 2
        # "self.pi" calls the class object into the method
        print("Area is: " + str(area))
        return area


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


# performs class constructor method
teaching_table = CircleInfo(36)


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
    if hasattr(entry, "count") is not True:
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


class Node:
    # Sets initial Node value and defaults downstream node value to None.
    def __init__(self, value, next_node=None):
        self.value = value
        # Used to identify downstream node.
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    # Replaces next_node with new node.
    def set_next_node(self, next_node):
        self.next_node = next_node


# Sets my_node's value and does not link to another node.
my_node = Node(2564)
# print(my_node.value)

# Sets your_node's value and becomes head node.
your_node = Node(42, my_node)

# Prints my_node's value.
print(your_node.next_node.value)


class LinkedList:
    def __init__(self, value=None):
        self.value = value
        # Creates a Node(value) and defines itself as the head node.
        # I wonder if this can be used to define a node in the middle
        # of a series since head_node is only defined here...
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        # Defines new_node as a new Node(value).
        new_node = Node(new_value)
        # Sets current instance of head_node as the next node in the series.
        new_node.set_next_node(self.head_node)
        # Then installs itself as the new head node.
        self.head_node = new_node

    # Their solution.
    def stringify_list(self):
        # Sets an empty string to fill.
        string_list = ""
        # Go to first node in series and evaluate that one first.
        current_node = self.get_head_node()
        # "while current_node:" evaluates to True, so this runs.
        while current_node:
            # Checks to make sure a value exists.
            if current_node.get_value() is not None:
                # Adds the value of the current node to the list with return.
                string_list += str(current_node.get_value()) + "\n"
            # Moves to the next node in the series.
            # If no next node exists, "while current_node:" == False
            # and the loop stops evaluating.
            current_node = current_node.get_next_node()
        return string_list

    # Define your remove_node method below:
    def remove_node(self, value_to_remove):
        # Starts evaluation at head node.
        current_node = self.head_node
        # If the current node is the one to remove, then...
        if current_node.get_value() == value_to_remove:
            print("if is working")
            # So if the head node is the one with the value we want to
            # remove, we just move on??? This doesn't make any sense and
            # solves nothing, and I hate it.
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node


# Yeah, of course it all prints fine.
# And they provide no notes as to why stringify_list works, they just assume
# you remember every single word and concept, no matter how briefly
# discussed or practiced.
linked_list = LinkedList(5)
linked_list.insert_beginning(70)
linked_list.insert_beginning(5675)
linked_list.insert_beginning(90)
print(linked_list.stringify_list())


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the pizza stack!".format(value))
        else:
            print("No room for {}!".format(value))

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Delivering " + item_to_remove.get_value())
            return item_to_remove.get_value()
        print("All out of pizza.")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0


# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
pizza_stack.pop()


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")

    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print(str("The " + item_to_remove.get_value()) + " is served!")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The queue is totally empty!")

    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print("No orders waiting!")

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0


print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #
# Uncomment the line below:
deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
# ------------------------ #
# Uncomment the line below:
deli_line.dequeue()


# ------------------------ #


class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        number_collisions = 1

        while (current_array_value[0] != key):
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1

        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions = 1

        while (possible_return_value != key):
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1

        return


hash_map = HashMap(20)
hash_map.assign("gabbro", "igneous")
hash_map.assign("sandstone", "sedimentary")
hash_map.assign("gneiss", "metamorphic")
print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss"))


class TreeNode:
    def __init__(self, value):
        self.value = value  # data
        self.children = []  # references to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            # Can also use "nodes_to_visit.extend(current_node.children)"
            nodes_to_visit += current_node.children


class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # HEAP HELPER METHODS
    # DO NOT CHANGE!
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    # NEW HELPER!
    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    # END OF HEAP HELPER METHODS

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None
        # Saves the desired return value.
        min = self.heap_list[1]
        print("Removing: {0} from {1}".format(min, self.heap_list))
        # Duplicates the last value over the desired value.
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        # Removes the duplicated value from the end of the list.
        self.heap_list.pop()
        print("Last element moved to first: {0}".format(self.heap_list))
        # Resorts the values to maintain heap rules.
        self.heapify_down()
        return min

    def add(self, element):
        self.count += 1
        print("Adding: {0} to {1}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            print("Heapifying down!")
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]
            if parent > child:
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent
            idx = smaller_child_idx

    print("Heap Restored! {0}".format(self.heap_list)

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:
                print("Left child is smaller")
                return self.left_child_idx(idx)
            else:
                print("Right child is smaller")
                return self.right_child_idx(idx)

    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
                tmp = self.heap_list[self.parent_idx(idx)]
                print("swapping {0} with {1}".format(tmp, self.heap_list[idx]))
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.parent_idx(idx)
        print("HEAP RESTORED! {0}".format(self.heap_list))
        print("")


# make an instance of MinHeap
min_heap = MinHeap()

# set internal list for testing purposes...
min_heap.heap_list = [None, 10, 13, 21, 61, 22, 23, 99]
min_heap.count = 7

while len(min_heap.heap_list) != 1:
    print(min_heap.heap_list)
    min_heap.retrieve_min()


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())


class Graph:
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value,
                                                      weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            print("Visiting " + current_vertex)
            if current_vertex == end_vertex:
                return True
            else:
                vertices_to_visit = set(
                    self.graph_dict[current_vertex].edges.keys())
                start += [vertex for vertex in vertices_to_visit if
                          vertex not in seen]
        return False


from random import randrange


def print_graph(graph):
    for vertex in graph.graph_dict:
        print("")
        print(vertex + " connected to")
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print("No edges!")
        for adjacent_vertex in vertex_neighbors:
            print("=> " + adjacent_vertex)


def build_graph(directed):
    g = Graph(directed)
    vertices = []
    for value in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        vertex = Vertex(value)
        vertices.append(vertex)
        g.add_vertex(vertex)

    for v in range(len(vertices)):
        v_idx = randrange(0, len(vertices) - 1)
        v1 = vertices[v_idx]
        v_idx = randrange(0, len(vertices) - 1)
        v2 = vertices[v_idx]
        g.add_edge(v1, v2, randrange(1, 10))

    print_graph(g)


build_graph(False)
