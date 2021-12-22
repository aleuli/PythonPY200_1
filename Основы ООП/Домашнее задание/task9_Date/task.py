class Date:
    def __init__(self, day: int, mounth: int, year: int):
        self.day = None
        self.mounth = None
        self.year = None
        self.init_day(day)
        self.init_mounth(mounth)
        self.init_year(year)

    def init_day(self, day: int) -> None:
        if not isinstance(day, int):
            raise TypeError

    def init_mounth(self, mounth: int) -> None:
        if not isinstance(mounth, int):
            raise TypeError

    def init_year(self, year: int) -> None:
        if not isinstance(year, int):
            raise TypeError

    def __str__(self) -> str:
        return f"День {self.day}, Месяц {self.mounth}, год {self.year}"

    def __repr__(self) -> str:
        return f"Date({self.day}, {self.mounth}, {self.year})"

if __name__ == '__main__':
    print()