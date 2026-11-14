class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self._shade_calls = 0
            self._is_tree = False

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def add_shade(self) -> None:
            self._shade_calls += 1

        def set_tree(self) -> None:
            self._is_tree = True

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )
            if self._is_tree:
                print(f"{self._shade_calls} shade")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height if height > 0 else 0.0
        self._age = age if age > 0 else 0
        self._stats = self._Stats()
        if height < 0:
            print(f"{self._name} Error, height can’t be negative")
        if age < 0:
            print(f"{self._name}Error, age can’t be negative")

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_stats(self) -> "_Stats":
        return self._stats

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
        self._stats.add_show()
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._age} days old"
        )

    def grow(self, hig: float = 2.1) -> None:
        self._stats.add_grow()
        self._height = self._height + hig

    def age(self, num_of_days: int = 1) -> None:
        self._stats.add_age()
        self._age = self._age + num_of_days


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
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


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats.set_tree()

    def produce_shade(self) -> None:
        self._stats.add_shade()
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


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("")
    print("=== Flower")
    Rose = Flower("Rose", 15.0, 10, "red")
    Rose.show()
    display_plant_statistics(Rose)
    print("[asking the rose to grow and bloom]")
    Rose.grow(8.0)
    Rose.bloom()
    Rose.show()
    display_plant_statistics(Rose)
    print("")
    print("=== Tree")
    Oak = Tree("Oak", 200.0, 365, 5.0)
    Oak.show()
    display_plant_statistics(Oak)
    print("[asking the oak to produce shade]")
    Oak.produce_shade()
    display_plant_statistics(Oak)
    print("")
    print("=== Seed")
    Sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    Sunflower.show()
    print("[make sunflower grow, age and bloom]")
    Sunflower.grow(30.0)
    Sunflower.age(20)
    Sunflower.bloom()
    Sunflower.show()
    display_plant_statistics(Sunflower)
    print("")
    print("=== Anonymous")
    Unknown = Plant.create_anonymous()
    Unknown.show()
    display_plant_statistics(Unknown)
