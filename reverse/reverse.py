class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head is None:  #if head is empty
            return None
        elif node.next_node: # if next exists
            new_node = node.get_next() # set the new node to the next one its pointing to
            self.reverse_list(new_node, node) #reset the function using the new node as node and node as prev
        else: #if there is no next node it has to be the tail,
            self.head = node #we set the tail as the head
        node.set_next(prev) #now set the next to the previous node


