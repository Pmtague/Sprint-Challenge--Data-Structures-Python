from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Ring buffer is empty
        if not self.storage.head:
            # Set the new item as the value of the head and the tail
            self.storage.add_to_head(item)
        # Ring buffer full
        elif self.storage.length == self.capacity:
            # If so, overwrite the current oldest
            if self.current == None:
                self.storage.head.value = item
                self.current = self.storage.head.next
            else:
                self.current.value = item
                self.current = self.current.next
        else:
            # Add the item to the tail (newest items)
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
