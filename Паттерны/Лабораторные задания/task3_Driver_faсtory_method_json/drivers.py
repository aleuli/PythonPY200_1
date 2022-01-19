import json
from typing import Sequence
from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Sequence:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Sequence) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class SimpleFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Sequence:
        with open(self.filename) as f:
            return [int(line) for line in f]

    def write(self, data: Sequence) -> None:
        with open(self.filename, "w") as f:
            for value in data:
                f.write(str(value))
                f.write('\n')

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


class JsonFileDriver():

    def __init__(self, filename):
        self.filename = None
        self.is_valid(filename)

    @staticmethod
    def is_valid(file):
        if not isinstance(file, list):
            raise TypeError

    def read(self):
        with open(self.filename) as f:
            return [line for line in f]

    def write(self, data):
        with open()




if __name__ == '__main__':
    write_data = [1, 2, 3]
    driver = SimpleFileDriver('tmp.txt')
    driver.write(write_data)

    read_data = driver.read()
    print(read_data)
