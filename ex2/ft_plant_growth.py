class Plant:
    name: str
    hight: float
    age: int

    def show(pl) -> None:
        print(f"{pl.name}: {round(pl.hight, 1)}cm, {pl.age} days old")

    def grow(p1) -> None:
        p1.hight = p1.hight + 0.8

    def age1(p1) -> None:
        p1.age = p1.age + 1


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.hight = 25.0
    rose.age = 30
    print("=== Garden Plant Growth ===")
    rose.show()
    i = 1
    groth = 0
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        groth = round(groth + 0.8, 1)
        rose.age1()
        rose.show()
    print(f"Growth this week: {groth}cm")
