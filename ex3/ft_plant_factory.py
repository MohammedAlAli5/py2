class Plant:
    def __init__(p1, name: str, hight: float, age: int) -> None:
        p1.name = name
        p1.hight = hight
        p1.age_days = age

    def show(pl) -> None:
        print(
            f"{pl.name}: {round(pl.hight, 1)}cm, "
            f"{pl.age_days} days old"
        )

    def grow(p1) -> None:
        p1.hight = p1.hight + 0.8

    def age(p1) -> None:
        p1.age_days = p1.age_days + 1


if __name__ == "__main__":
    Rose = Plant("Rose", 25.0, 30)
    Oak = Plant("Oak", 200.0, 365)
    Cactus = Plant("Cactus", 5.0, 90)
    Sunflower = Plant("Sunflower", 80.0, 45)
    Fern = Plant("Fern", 15.0, 120)
    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    Rose.show()
    print("Created: ", end="")
    Oak.show()
    print("Created: ", end="")
    Cactus.show()
    print("Created: ", end="")
    Sunflower.show()
    print("Created: ", end="")
    Fern.show()
