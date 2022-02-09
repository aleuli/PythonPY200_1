import json
from typing import Iterable
from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Iterable:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Iterable) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class SimpleFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Iterable:
        with open(self.filename) as f:
            return [int(line) for line in f]

    def write(self, data: Iterable) -> None:
        with open(self.filename, "w") as f:
            for value in data:
                f.write(str(value))
                f.write('\n')

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


class JsonFileDriver(IStructureDriver):

    def __init__(self, json_filename):
        self.json_filename = json_filename

    def read(self) -> Iterable:
        with open(self.json_filename) as f:
            js = json.load(f)
        if not isinstance(js, list):
            raise TypeError
        return js

    def write(self, data: Iterable) -> None:
        data = [value for value in data]
        with open(self.json_filename, "w") as file:
            json.dump(data, file)

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.json_filename}\")"





if __name__ == "__main__":
    # Write your solution here
    pass
