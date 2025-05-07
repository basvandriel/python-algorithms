from collections.abc import Generator
from typing import Optional
from linkedlist_node import Node


class NonSortedLinkedList:
    head: Optional[Node]

    def __init__(self):
        self.head = None

    @property
    def tail(self) -> Node | None:
        """The place where the next value should be filled in"""

        if not self.head:
            return None

        if self.head.next is None:
            return self.head

        return self.head.find_deepest_node()

    def is_empty(self) -> bool:
        return self.head is None

    def insert(self, value: int) -> None:
        tail = self.tail

        if not self.tail:
            self.head = Node(value, None)
        else:
            tail.next = Node(value, None)

    def __iter__(self) -> Generator[int]:
        current = self.head

        while current is not None:
            yield current.value
            current = current.next

    def delete(self, value: int) -> int:
        """returns the delete count"""
        delete_count = 0

        if self.head and self.head.value == value:
            self.head = self.head.next
            delete_count += 1

        # Now, next is not None. Let's find the values
        # Find the value
        current: Optional[Node] = self.head

        # Before we start doing this, first check the head value
        while current and current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                delete_count += 1
            else:
                current = current.next

        return delete_count
