class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    # Sets new next_node
    def set_next_node(self, next_node):
        self.next_node = next_node


# Sets my_node's value and does not link to another node
my_node = Node(2564)
print(my_node.value)

# Sets your_node's value and links to my_node
your_node = Node(42, my_node)
# Prints my_node's value
print(your_node.next_node.value)


class LinkedList:
    def __init__(self, value=None):
        self.value = value
        # Sets head_node as value, even when no value is passed in????
        # Does that mean head_node == None by default????? that seems odd
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        # Defines new_node as Node class
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    # Their solution
    def stringify_list(self):
        string_list = ""
        # Oh, you can just define "here" and say "while you're here"
        # Fuck me, I guess
        current_node = self.get_head_node()
        # while current_node: evaluates to True, so this runs.
        while current_node:
            # Checks to make sure a value exists
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

# Yeah, of course it all prints fine.
# And they provide no notes as to why stringify_list works, they just assume
# you remember every single word and concept, no matter how briefly
# discussed or practiced.
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())
