from typing import Any, Optional, Union


class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """

        :param value: Любое значение которое помещено в узел
        :param next_: следующий узел , если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter , обращение к свойству

    def __str__(self) -> str:
        """

        :return: возвращаем читабельную строку
        """
        return str(self.value)

    def __repr__(self) -> str:
        """

        :return: возвращает "cырые" данные для внутреннего представления
        """

        return f"Node({self.value}, {None})" if {self.next} is None \
            else f"Node(Node({self.value}), Node({self.next}))"

    @staticmethod
    def is_valid(node: Optional["Node"]) -> None:
        if not isinstance(node, (Node, type(None))):
            raise TypeError("узел должен быть либо None, либо Node")

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"] = None) -> None:
        print("вызван магический метод __setter__")
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    """
    Класс который описывает двойные связные узлы
    """
    def __init__(self, value: Any, next_: Union[Optional["Node"], Optional["DoubleLinkedNode"]] = None,
                 prev: Union[Optional["Node"], Optional["DoubleLinkedNode"]] = None):
        """

        :param value: Любое значение которое наследуется от класса Node
        :param next_: следующй узел наследуемый от класса Node
        :param prev: Предыдущий узел , если он есть
        """
        super().__init__(value, next_)
        self.prev = prev

    @staticmethod
    def is_valid_prev(doublelinkednode: Optional["DoubleLinkedNode"]) -> None:
        if not isinstance(doublelinkednode, (type(None), DoubleLinkedNode)):
            raise TypeError("узел должен быть либо None, либо DoubleLinkedNode")

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Union[Optional["Node"], Optional["DoubleLinkedNode"]] = None) -> None:
        print("вызван магический метод __setter__ из DoubleLinkedNode")
        self.is_valid_prev(prev)
        self._prev = prev

    def __repr__(self) -> str:
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
