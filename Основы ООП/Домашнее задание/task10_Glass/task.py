from typing import Any


class Glass:

    def __init__(self, material: Any):
        """
        Инициализируем обьект Glass

        :param material: принимаем атрибут
        """
        self.material = material

    def get_material(self) -> None:
        """
        Метод возврата атрибута

        :return: возврата атрибута
        """
        return self.material


if __name__ == "__main__":
    glass = Glass(100)
    print(glass)
