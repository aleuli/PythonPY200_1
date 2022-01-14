from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):

    """Класс, который описывает узел двусвязного списка. """

    def __init__(self, value, next_=None, prev=None):
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self) -> str:
        next_ = str(None) if self.next is None \
            else f"{self.__class__.__name__},{self.next.value}, {None}, {None}"
        return f"{self.__class__.__name__}({self.value}, {self.next},{self.prev})"

        # return f"DoubleLinkedNode({self.value}, {self.next_}, {None})" if self.prev is None \
        #     else f"DoubleLinkedNode({self.value}), DoubleLinkedNode({self.next_}, DoubleLinkedNode({self.prev})"

    #todo getter and setter for prev
    #repr переопределяем
    # str наследуем
    # is_valid переопределяем
    # setter and getter наследуем


first_node = "first"
second_node = "second"
presecond_node = "presecond_node"

