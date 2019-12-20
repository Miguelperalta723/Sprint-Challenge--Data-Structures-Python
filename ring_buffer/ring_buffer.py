from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #if capacity is full
        if len(self.storage) == self.capacity:
            #if current is none movve tot he end
            if self.current is None:
                self.current = self.storage.tail
            #if it had a value set it to item
            self.current.value = item
            #if there is a previous set it as current, if not set to tail
            if self.current.prev:
                self.current = self.current.prev
            else:
                self.current = self.storage.tail
        #if its not full add to the head
        elif len(self.storage) < self.capacity:
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.tail
        while node:
            if node.value is not None:
                list_buffer_contents.append(node.value)
            node = node.prev
            


        return list_buffer_contents
# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
