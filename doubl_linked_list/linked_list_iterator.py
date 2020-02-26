from custom_linked_list.node import Node


class LinkedListIterator:
    def __init__(self, first: Node) -> None:
        self.first = first

    def __next__(self) -> Node:
        while self.first is not None:
            current = self.first
            self.first = self.first.next
            return current
        raise StopIteration
