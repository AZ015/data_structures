from typing import Union

from doubl_linked_list import LinkedListIterator
from doubl_linked_list.node import Node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self):
        return self._size

    def insert_first(self, data: Union[int, float]) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.last = new_node
        else:
            self.first.prev = new_node
        new_node.next = self.first
        self.first = new_node
        self._size += 1

    def insert_last(self, data: Union[int, float]) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.last = new_node
        else:
            self.last.next = new_node
        new_node.prev = self.last.next
        self.last.next = new_node
        self.last = new_node
        self._size += 1

    def insert(self, new_node: Node) -> Union[str, Node]:
        current = self.first
        if current == self.last:
            new_node.next = None
            self.last = new_node
        else:
            new_node.next = current.next
            current.next.prev = new_node

        new_node.prev = current
        current.next = new_node
        self._size += 1
        return current

    def remove(self, value) -> Union[str, Node]:
        current = self.first
        previous = self.first
        while current.data != value:
            if current.next is None:
                return "Can't delete, value isn't exist in the list"
            else:
                previous = current
                current = current.next
        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next
        self._size -= 1
        return current

    def remove_first(self) -> None:
        tmp = self.first
        if self.first.next is None:
            self.last = None
        else:
            self.first.next.previous = None
        self.first = self.first.next
        self._size -= 1
        return tmp

    def remove_last(self) -> None:
        tmp = self.last
        if self.first.next is None:
            self.first = None
        else:
            self.last.previous.next = None
        self.last = self.last.previous
        self._size -= 1
        return tmp

    def display_list(self) -> None:
        current: Node = self.first
        while current is not None:
            current.display_data()
            current = current.next

    def __iter__(self):
        return LinkedListIterator(self.first)


if __name__ == '__main__':
    lst = DoublyLinkedList()
    lst.insert_first(12)
    lst.insert_first(13)
    lst.insert_first(14)
    lst.insert(Node(145))
    lst.insert_first(15)
    lst.display_list()

    # lst.remove(13)
    # for item in lst:
    #     print(item.data)
