from custom_linked_list.node import Node


class LinkedListIterator:
    def __init__(self, root: Node) -> None:
        self.root = root

    def __next__(self) -> Node:
        while self.root is not None:
            current = self.root
            self.root = self.root.next
            return current
        raise StopIteration
