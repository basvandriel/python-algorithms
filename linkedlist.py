from dataclasses import dataclass
from typing import Generator, Optional, Self


@dataclass
class Node[T: int]:
    value: T
    next: Optional["Node[T]"]

    @property
    def depth(self):
        if self.next is None:
            return 0
        return 1 + self.next.depth

    @property
    def size(self):
        if self.next is None:
            return 1
        return 1 + self.next.size

    def find_deepest_value(self) -> int:
        # There is no next value, this is the deepest
        if self.next is None:
            return self.value
        return self.next.find_deepest_value()

    def find_deepest_node(self) -> "Node":
        if self.next is None:
            return self
        return self.next.find_deepest_node()


def build_node(data: list[int], index: int = 0) -> Optional[Node[int]]:
    out_of_bounds: bool = index > (len(data) - 1)

    if out_of_bounds:
        return None

    next_item = build_node(data, index + 1)

    return Node(data[index], next_item)


class SortedLinkedList:
    head: Optional[Node]

    def __init__(self) -> None:
        self.head = None

    def _find_node_in_middle(self, value: int) -> Node:
        # For example, we have our head like 1,4,5,
        # this method should return the first head
        current = self.head

        # The next node should always be lower then the input
        while current.next and current.next.value < value:
            current = self.head.next

        return current

    def insert(self: Self, value: int):
        node = Node(value, None)

        # This is the first time the node gets build
        if not self.head:
            self.head = node
            return

        # Swap the current next and current values
        if value < self.head.value:
            self.head.next = self.head
            self.head.value = value
            return

        deepest_node = self.head.find_deepest_node()

        # This is the case where we put it at the end of the list (the input number is bigger then the latest value)
        if value >= deepest_node.value:
            deepest_node.next = node
            return

        # Find the node where to put the value in the 'next' attribute
        middle_node = self._find_node_in_middle(value)

        # For the current node, set the old value in the next value
        node.next = middle_node.next

        # And vica versa
        middle_node.next = node

    def delete_first_value(self: Self, value: int) -> int:
        return self.delete_value(value, True)

    def delete_value(self: Self, value: int, only_delete_first: bool = False) -> int:
        """returns the amount of deleted values"""
        # No data to delete
        if not self.head:
            return 0

        # direct match but with no next one
        if self.head.value == value and self.head.next is None:
            self.head = None
            return 1

        delete_count = 0

        # TODO search for the values to delete
        current = self.head

        # We always check the next => the head has already been checked
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                delete_count += 1

                if only_delete_first:
                    break
            else:
                current = current.next

        return delete_count

    def __iter__(self) -> Generator[int, None, None]:
        current: Optional[Node] = self.head

        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self.head.size
