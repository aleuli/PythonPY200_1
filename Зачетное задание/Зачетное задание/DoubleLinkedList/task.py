from collections.abc import MutableSequence

from typing import Any, Iterable, Optional

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):

    CLASS_NODE = Node

    """Конструктор связного списка."""

    def __init__(self, data: Iterable = None):
        self._len = 0
        self._head = None
        self._tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """Добавление элементов в конец связного списка."""

        append_node = self.CLASS_NODE(value)
        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """Функция выполняет перемещение по узлам до указанного индекса.И возвращает узел."""

        if not isinstance(index, int):
            raise TypeError("Ошибка типа.")

        if not 0 <= index < self._len:
            raise IndexError("Ошибка индекса.")

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """Функция которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел

        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """Метод возвращает значение узла по указанному индексу."""

        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """Метод устанавливает значение узла по указанному индексу."""

        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int) -> None:
        """Удаление элементов по ключу."""

        if not isinstance(index, int):
            raise TypeError("Неправильный тип.")

        if not 0 <= index < self._len:
            raise IndexError("Неправильный индекс(граница).")

        if index == 0:
            self._head = self._head.next
        elif index == self._len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next
            self.linked_nodes(prev_node, next_node)
        self._len -= 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __str__(self) -> str:
        """Человекочитаемое представление обьекта."""

        return f"{self.to_list()}"

    def __repr__(self) -> str:
        """Возврат представления обьекта."""

        return f"{self.__class__.__name__}({self.to_list()})"

    def __len__(self):
        """Возвращает количество элементов."""

        return self._len

    # def nodes_iterator(self) -> Iterator[Node]:
    #     """Генератор для прохода по всем узлам."""
    #
    #     current_node = self._head
    #     for _ in range(self._len):
    #         yield current_node
    #     current_node.next = current_node
    #
    # def __iter__(self) -> Iterator[Any]:
    #     """Метод возвращает узел по которому итерировался."""
    #
    #     return self.nodes_iterator()
    #
    # def __contains__(self, item) -> bool:
    #     """Метод проверяет вхождение обьекта в последовательность."""
    #
    #     for node in self.nodes_iterator():
    #         if node.value == item:
    #             return True
    #     return False
    #
    # def __reversed__(self):
    #     ...
    #
    # def count(self, value: Any) -> int:
    #     ...
    #
    # def pop(self, index: int = ...):
    #     ...
    #
    # def extend(self, values: Iterable[...]) -> None:
    #     ...
    #
    # def remove(self, value: ...) -> None:
    #     ...
    #
    # def index(self, value: Any, start: int = ..., stop: int = ...) -> int:
    #     ...

    def insert(self, index: int, value: Any) -> None:
        """Добавляет значение в список по указанному индексу."""

        if not isinstance(index, int):
            raise TypeError

        if index < 0:
            raise IndexError

        if index >= self._len:
            self.append(value)

        if 0 < index < self._len:
            insert_node = Node(value)
            current_node = self.step_by_step_on_nodes(index - 1)
            next_node = current_node.next
            self.linked_nodes(insert_node, next_node)
            self.linked_nodes(current_node, insert_node)
            self._len += 1

        if index == 0:
            # insert_node = Node(value)
            # insert_node.next = self._head
            # self._head.prev = insert_node
            # self._head = insert_node
            insert_node = Node(value)
            insert_node.next = self._head
            self._head = insert_node
            self._len += 1


class DoubleLinkedList(LinkedList):

    CLASS_NODE = DoubleLinkedNode

    """Конструктор двухсвязного списка."""

    def __init__(self, data: Iterable, prev: Optional["DoubleLinkedNode"]):
        super().__init__(data)
        self.prev = prev

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional["DoubleLinkedNode"] = None) -> None:
        """Функция которая связывает между собой три узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """

        left_node.next = right_node
        right_node.prev = left_node


if __name__ == "__main__":

    list_ = [1, 2, 3]
    linked_list = LinkedList(list_)
    print(linked_list)

    linked_list.append(100)  # метод append
    print(linked_list)

    print(linked_list.step_by_step_on_nodes(2))  # метод step_by_step_on_nodes

    first_node = Node(1)
    second_node = Node(2)
    linked_list.linked_nodes(first_node, second_node)
    print(repr(first_node), repr(second_node))  # метод linked_nodes

    print(linked_list[2])  # метод getitem

    linked_list[2] = 5
    print(linked_list)  # метод setitem

    del linked_list[2]
    print(linked_list)  # метод del

    print([link for link in linked_list])  # метод to_list

    print(str(linked_list))  # метод str

    print(repr(linked_list))  # метод repr

    print(len(linked_list))  # метод len

    linked_list.insert(2, 50)
    print(linked_list)  # метод insert

    double_first_node = DoubleLinkedNode(1)
    double_second_node = DoubleLinkedNode(2)
    double_first_node.next = double_second_node
    double_second_node.prev = double_first_node
    print(repr(double_first_node), repr(double_second_node))  # реализация двусвязного списка
