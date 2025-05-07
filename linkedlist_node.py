from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    next: Optional["Node"]

    @property
    def size(self):
        if self.next is None:
            return 1
        return 1 + self.next.size

    def find_deepest_value(self) -> int:
        return self.find_deepest_node().value

    def find_deepest_node(self) -> "Node":
        if self.next is None:
            return self
        return self.next.find_deepest_node()
