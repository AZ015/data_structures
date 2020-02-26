from typing import Union


class Node:
    def __init__(self, data: Union[int, float]) -> None:
        self.data = data
        self.next = None

    def display_link(self) -> None:
        print(f"{self.data} ->", end=" ")
