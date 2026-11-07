class Plant:
    def __init__(p1, name: str, hight: float, age: int):
        p1._name = name
        p1._hight = hight if hight >= 0 else 0.0
        p1._age = age if age >= 0 else 0
        if hight <= 0:
            print(f"{p1._name} Error, height can’t be negative")
        if age <= 0:
            print(f"{p1._name}Error, age can’t be negative")

    def get_hight(p1) -> float:
        return p1._hight

    def get_age(p1) -> int:
        return p1._age

    def set_hight(p1, hight: float) -> None:
        if hight <= 0:
            print(f"{p1._name} Error, height can’t be negative")
        else:
            p1._hight = hight
            print(f"Height updated: {p1._hight}cm")

    def set_age(p1, age: int) -> None:
        if age <= 0:
            print(f"{p1._name}Error, age can’t be negative")
        else:
            p1._age = age
            print(f"Age updated: {p1._age} days")

    def show(pl) -> None:
        print(f"{pl._name}: {round(pl._hight, 1)}cm, {pl._age} days old")

    def grow(p1) -> None:
        p1._hight = p1._hight + 0.8

    def age1(p1) -> None:
        p1._age = p1._age + 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    Rose = Plant("Rose", 15.0, 10)
    Rose.show()
    print("")
    Rose.set_hight(25)
    Rose.set_age(30)
    print("")
    Rose.set_hight(-25)
    Rose.set_age(-30)
    print("Current state: ", end="")
    Rose.show()
