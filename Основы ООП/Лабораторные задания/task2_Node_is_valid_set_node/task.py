from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.next = None
        self.next = next_
        self.node = None
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        # TODO установить значение следующего узла с помощью метода set_next
    def set_next(self, next_: Optional["Node"]) -> None:
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        # TODO метод проверки корректности связываемого узла
        if not isinstance(node, (type(None), Node)):
            raise TypeError
        self.node = node

    def set_next_1(self, next_: Optional["Node"] = None) -> None:

        if not isinstance(next_, (type(None), Node)):
            raise TypeError
        self.next = next_


if __name__ == '__main__':

    first_node = Node(1)
    second_node = Node(2)
    first_node.next = second_node
    # TODO свяжите первый узел со вторым

    print(first_node)
    print(second_node)
