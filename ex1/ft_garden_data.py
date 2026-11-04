class Plant:
    name : str
    hight : int
    age : int
    def show(pl) -> None:
        print(f"{pl.name}: {pl.hight}cm, {pl.age} days old")
if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.hight = 25
    rose.age = 30
    Sunflower = Plant()
    Sunflower.name = "Sunflower"
    Sunflower.hight = 80
    Sunflower.age = 45
    Cactus = Plant()
    Cactus.name = "Cactus"
    Cactus.hight = 15
    Cactus.age = 120
    rose.show()
    Sunflower.show()
    Cactus.show()
