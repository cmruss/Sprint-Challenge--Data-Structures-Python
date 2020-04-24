from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the RingBuffer is full
        if self.storage.__len__() == self.capacity:
            # and current node is none
            if not self.current:
                # make the tail of the dll the current node
                self.current = self.storage.tail
            # set the current value to the passed in item value
            self.current.value = item
            # set the current node to the previous node
            self.current = self.current.prev
        else:
            # add the passed in value to the head if RingBuffer is not at capacity
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        tail = self.storage.tail 

        while tail:
            list_buffer_contents.append(tail.value)
            tail = tail.prev

        # TODO: Your code here        

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
