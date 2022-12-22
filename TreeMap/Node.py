from dataclasses import dataclass
from typing import Any
from TreeMap.Color import Color


@dataclass
class Node:
    key: Any
    val: Any
    color: Color
    parent: object
    left: object
    right: object

    def __str__(self) -> str:
        return f'\t\tKey: {self.key} Val: {self.val}; Color: {self.color}; Parent:{self.parent.key if self.parent is not None else self.parent}\n Left:{self.left.key}\t\t\t Right:{self.right.key}'

    def grand_parent(self):
        if self.parent is not None:
            return self.parent.parent
        else:
            return None

    def uncle(self):
        gp = self.grand_parent()
        if gp is None:
            return None
        if self.parent is gp.left:
            return gp.right
        else:
            return gp.left
        
    def sibling(self):
        if self.parent is None:
            return None
        if self is self.parent.left:
            return self.parent.right
        else:
            return self.parent.left

