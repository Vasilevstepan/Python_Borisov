class Cat:
    cat_count = 0
    def __init__(self,name,age,toy):
        self.name = name
        self.age = age
        self.toy = toy
        Cat.cat_count += 1
    def display(self):
        print(f"Вашу кошку зовут {self.name}, ей {self.age} года и ее любимая игрушка {self.toy}")

cat1 = Cat("Pusha", 3, "Mini-cat")
cat2 = Cat("Kitty", 4, "Ball")


class War_cat(Cat):
    def __init__(self,name,age,toy,weapon):
        Cat.__init__(self,name,age,toy)
        self.weapon = weapon
    def display(self):
        print(f"Вашу кошку зовут {self.name}, ей {self.age} года и ее любимая игрушка {self.toy} в ее арсенала {self.weapon}")
    def display_count(self):
        print(f"Всего кошек {Cat.cat_count}")
        
cat1 = War_cat("Pusha", 3, "Mini-cat", 'knife')
cat2 = War_cat("Kitty", 4, "Ball", "gun")

cat2.display()
cat1.display()
cat2.display_count()