from typing import Any, Optional


class Node:
    """ Класс который описывает узел связного списка """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """

        :param value: Любое значение которое помещено в узел
        :param next_: Следующий узел , если он есть
        """

        self.value = value
        self.next = next_

    @staticmethod
    def is_valid(node: Optional["Node"]) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if {self.next} is None \
            else f"Node(Node({self.value}), Node({self.next}))"

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"] = None) -> None:
        self.is_valid(next_)
        self._next = next_


if __name__ == '__main__':
    first_node = Node(1)
    first_node.next = Node(2)
    print(repr(first_node), repr(first_node.next))
