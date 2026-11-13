class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height if height > 0 else 0.0
        self._age = age if age > 0 else 0
        if height < 0:
            print(f"{self._name} Error, height can’t be negative")
        if age < 0:
            print(f"{self._name}Error, age can’t be negative")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name} Error, height can’t be negative")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:

            print(f"{self._name}Error, age can’t be negative")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._age} days old"
        )

    def grow(self, hig: float) -> None:
        self._height = self._height + hig

    def age(self, num_of_days: int) -> None:
        self._age = self._age + num_of_days


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloming = False

    def bloom(self) -> None:
        self._bloming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self._bloming:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")


class Tree (Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, hig: float = 2.1) -> None:
        super().grow(hig)

    def age(self, num_of_days: int = 1) -> None:
        super().age(num_of_days)
        self.nutritional_value += num_of_days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    Rose = Flower("Rose", 15.0, 10, "red")
    Rose.show()
    print("[asking the rose to bloom]")
    Rose.bloom()
    Rose.show()
    print("")
    print("=== Tree")
    Oak = Tree("Oak", 200.0, 365, 5.0)
    Oak.show()
    print("[asking the oak to produce shade]")
    Oak.produce_shade()
    print("")
    print("=== Vegetable")
    Tomato = Vegetable("Tomato", 5.0, 10, "April")
    Tomato.show()
    print("[make tomato grow and age for 20 days]")
    Tomato.age(20)
    Tomato.grow(42)
    Tomato.show()
