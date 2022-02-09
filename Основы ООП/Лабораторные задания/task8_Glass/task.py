from typing import Union


class Glass:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        self.capacity_volume = None
        self.occupied_volume = None
        self.init_capacity_volume(capacity_volume)
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume: Union[int, float]) -> None:
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume: Union[int, float]) -> None:
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume <= 0:
            raise ValueError
        self.occupied_volume = occupied_volume

    def add_water(self, water_1: Union[int, float]) -> None:
        if not isinstance(water_1, (int, float)):
            raise TypeError
        if water_1 < 0:
            raise ValueError
        if (self.capacity_volume - self.occupied_volume - water_1) < 0:
            raise ValueError
        self.occupied_volume += water_1

    def remove_water(self, water_2: Union[int, float]) -> None:
        if not isinstance(water_2, (int, float)):
            raise TypeError
        if water_2 < 0:
            raise ValueError
        if (self.occupied_volume - water_2) < 0:
            raise ValueError
        self.occupied_volume -= water_2


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
    glass.add_water(100)
    print(glass.capacity_volume, glass.occupied_volume)
    glass.remove_water(200)
    print(glass.capacity_volume, glass.occupied_volume)
