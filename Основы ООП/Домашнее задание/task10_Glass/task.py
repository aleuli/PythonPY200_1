from typing import Any


class Glass:
    def __init__(self, material: Any):
        self.material = material

    def get_material(self):
        return self.material


if __name__ == "__main__":
    print(Glass.get_material())
