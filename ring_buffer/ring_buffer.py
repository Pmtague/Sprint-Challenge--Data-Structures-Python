from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Is the ring buffer at capacity?
        # If yes:
        if self.capacity == self.storage.length:
            # 	Store the value of the current head (oldest)
            curr_val = self.storage.head.value
            #   Overwrite the current head with the newest value
            self.storage.head = item
            #   Move the oldest marker to the next element
            self.oldest = self.storage.head.next
        # If no, add the item to the next available slot
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        if self.storage.head == None:
            return None

        if self.storage.head == self.storage.tail:
            list_buffer_contents.append(self.storage.head.value)

        else:
            current = self.storage.head
            while current != None:
                list_buffer_contents.append(current.value)
                current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
