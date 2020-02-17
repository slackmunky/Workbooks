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


# Our LinkedList class
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


linked_list = LinkedList(5)
linked_list.insert_beginning(70)
linked_list.insert_beginning(5675)
linked_list.insert_beginning(90)
linked_list.remove_node(90)