class Plant:
    name: str
    hight: float
    age_days: int

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
    rose = Plant()
    rose.name = "Rose"
    rose.hight = 25.0
    rose.age_days = 30
    print("=== Garden Plant Growth ===")
    rose.show()
    groth = 0.0
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        groth = round(groth + 0.8, 1)
        rose.age()
        rose.show()
    print(f"Growth this week: {groth}cm")
