from typing import Any
from typing import Optional


class Node:
    """Класс, который описывает узел связного списка."""

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """

        :param value: Любое значение которое помещено в узел.
        :param next_: Cледующий узел , если он есть.

        """
        self.value = value
        self.next = next_  # Вызовется setter , обращение к свойству.

    def __str__(self) -> str:
        """Метод возвращает человекочитаемую строку."""

        return str(self.value)

    def __repr__(self) -> str:
        """Метод возвращает "cырые" данные для внутреннего представления."""

        return f"Node({self.value}, {None})" if {self.next} is None \
            else f"Node(Node({self.value}), Node({self.next}))"

    @staticmethod
    def is_valid(node: Optional["Node"]) -> None:
        if not isinstance(node, (Node, type(None))):
            raise TypeError("Ошибка типа - is_valid.")

    @property
    def next(self):
        """Getter."""

        return self._next

    @next.setter
    def next(self, next_: Optional["Node"] = None) -> None:
        """Setter."""

        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    """Класс который описывает двойной связный узел."""

    def __init__(self, value: Any, next_: Node = None, prev: Optional["DoubleLinkedNode"] = None):
        """

        :param value: Любое значение которое наследуется от класса Node
        :param next_: следующй узел наследуемый от класса Node
        :param prev: Предыдущий узел , если он есть

        """
        super().__init__(value, next_)
        self.prev = prev  # Вызовется setter , обращение к свойству.

    @staticmethod
    def is_valid_prev(doublelinkednode: Optional["DoubleLinkedNode"]) -> None:
        if not isinstance(doublelinkednode, (type(None), DoubleLinkedNode)):
            raise TypeError("Ошибка типа - Is_valid_prev.")

    @property
    def prev(self):
        """Getter."""

        return self._prev

    @prev.setter
    def prev(self, prev: Optional["DoubleLinkedNode"] = None) -> None:
        """Setter."""

        self.is_valid_prev(prev)
        self._prev = prev

    def __repr__(self) -> str:
        """Метод возвращает "cырые" данные для внутреннего представления."""

        next_ = str(None) if self.next is None \
            else f"{self.__class__.__name__}({self.next})"
        prev = str(None) if self.prev is None \
            else f"{self.__class__.__name__}({self.prev})"
        return f"{self.__class__.__name__}(DoubleLinkedNode({self.value}), {next_}, {prev})"


if __name__ == "__main__":
    first_node = Node(1)
    second_node = Node(2)
    first_node.next = second_node
    last_node = Node(3)
    second_node.next = last_node
    print(repr(first_node), repr(second_node), repr(last_node))

    a = DoubleLinkedNode(1)
    b = DoubleLinkedNode(2)
    c = DoubleLinkedNode(3)
    a.next = b
    b.prev = a
    b.next = c
    c.prev = b
    print(repr(a), repr(b), repr(c))
