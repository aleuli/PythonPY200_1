class Date:
    def __init__(self, day: int, mounth: int, year: int):
        """
        Инициализируем класс Date

        :param day: задаем день
        :param mounth: задаем месяц
        :param year: задаем год
        """
        self.day = None
        self.mounth = None
        self.year = None
        self.init_day(day)
        self.init_mounth(mounth)
        self.init_year(year)

    def init_day(self, day: int) -> None:
        if not isinstance(day, int):
            raise TypeError
        if day < 10:
            day = "0" + str(day)
        self.day = day

    def init_mounth(self, mounth: int) -> None:
        if not isinstance(mounth, int):
            raise TypeError
        if mounth < 10:
            mounth = "0" + str(mounth)
        self.mounth = mounth

    def init_year(self, year: int) -> None:
        if not isinstance(year, int):
            raise TypeError
        self.year = year

    def __str__(self) -> str:
        return f"{self.day}/{self.mounth}/{self.year}"

    def __repr__(self) -> str:
        return f"Date({self.day}, {self.mounth}, {self.year})"


if __name__ == '__main__':
    data = Date(1, 1, 2021)
    print(str(data))
    print(repr(data))
