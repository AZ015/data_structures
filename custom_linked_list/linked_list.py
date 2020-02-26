from typing import Union

from custom_linked_list.linked_list_iterator import LinkedListIterator
from custom_linked_list.node import Node


class LinkedList:
    def __init__(self) -> None:
        self.root = None
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self):
        return self._size

    def insert_first(self, data: Union[int, float]) -> None:
        node = Node(data)
        node.next = self.root
        self.root = node
        self._size += 1

    def insert(self, data: Union[int, float]) -> None:
        node = Node(data)
        current = self.root
        while current.next is not None:
            current = current.next
        current.next = node
        self._size += 1
        return current

    def insert_after(self, data: Union[int, float], new_node: Node) -> Union[str, Node]:
        current = self.root
        previous = self.root
        while current.data != data:
            if current.next is None:
                return "Can't insert"
            else:
                previous = current
                current = current.next
        previous.next = new_node
        new_node.next = current
        self._size += 1
        return current

    def remove_first(self) -> None:
        tmp = self.root
        self.root = tmp.next
        self._size -= 1
        return tmp

    def remove(self, value) -> Union[str, Node]:
        current = self.root
        previous = self.root
        while current.data != value:
            if current.next is None:
                return "Can't delete, value isn't exist in the list"
            else:
                previous = current
                current = current.next
        if current == self.root:
            self.root = self.root.next
        else:
            previous.next = current.next
        self._size -= 1
        return current

    def display_list(self) -> None:
        current: Node = self.root
        while current is not None:
            current.display_link()
            current = current.next

    def find(self, value):
        current = self.root
        while current.data != value:
            if current.next is None:
                return False
            else:
                current = current.next
        return True

    def __iter__(self):
        return LinkedListIterator(self.root)


if __name__ == '__main__':
    lst = LinkedList()
    lst.insert_first(12)
    lst.insert_first(13)
    lst.insert_first(14)
    lst.insert_first(15)
    lst.insert_after(14, Node(34))
    for item in lst:
        print(item.data)
