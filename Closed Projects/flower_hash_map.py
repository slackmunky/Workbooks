flower_definitions = [['begonia', 'cautiousness'],
                      ['chrysanthemum', 'cheerfulness'],
                      ['carnation', 'memories'],
                      ['daisy', 'innocence'],
                      ['hyacinth', 'playfulness'],
                      ['lavender', 'devotion'],
                      ['magnolia', 'dignity'],
                      ['morning glory', 'unrequited love'],
                      ['periwinkle', 'new friendship'],
                      ['poppy', 'rest'],
                      ['rose', 'love'],
                      ['snapdragon', 'grace'],
                      ['sunflower', 'longevity'],
                      ['wisteria', 'good luck']
                      ]


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def insert(self, new_node):
        current_node = self.head_node

        if not current_node:
            self.head_node = new_node

        while current_node:
            next_node = current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
            current_node = next_node

    def __iter__(self):
        current_node = self.head_node
        while current_node:
            yield current_node.get_value()
            current_node = current_node.get_next_node()


class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(self.array_size)]

    # Translates key string into hashable code.
    def hash(self, key):
        key_digits = key.encode()
        hash_code = sum(key_digits)
        # Can also be "return sum(key.encode())", but we want clarity in steps.
        return hash_code

    # Finds index within array for hashed key.
    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        # Can also be "self.array[self.compress(self.hash(key))] = [key,
        # value]", maybe? But that's kinda complicated. Show your work.
        hashed_key = self.hash(key)
        array_index = self.compress(hashed_key)
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        for item in list_at_array:
            if key == item[0]:
                item[1] = value
                return
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        # payload is the current_array_index with a different name.
        list_at_index = self.array[array_index]

        for item in list_at_index:
            if key == item[0]:
                return item[1]
        return None


blossom = HashMap(14)

for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

print(blossom.retrieve("wisteria"))