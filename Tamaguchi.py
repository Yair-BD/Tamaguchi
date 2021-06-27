def animal():
    import os
    class Animal:

        def __init__(self, name):
            self.name = name
            self._hunger = 0
            self._fun = 0

        def play(self):
            self._fun += 1
            self._hunger += 1
            return "It's so fun to play with you ^_^"

        def eat(self):
            if self._hunger > 0:
                self._hunger -= 1
            else:
                print("but i'm already satiate ")

        def go_to_toilet(self):
            self._hunger += 1

        def print_hunger(self):
            print(self._hunger)

        def __str__(self):
            return f"My name is {self.name} and i love u ^_^ \n" \
                   f"my level of hunger is {self._hunger} \nof fun is {self._fun} ^_^ "

    class Turtle(Animal):

        def __init__(self, name, color, armor=0, home=0):
            Animal.__init__(self, name)
            self.t_color = color
            self.p_armor = armor
            self.e_home = home

        def buy(self):
            gift = input("What do you give mee ? \n")
            self.e_home += gift
            return "Ho i'm preshiat that"

        def eat(self):
            print("Ho good hasa for a good filling")
            return super(Turtle, self).eat()

    class Dog(Animal):

        def __init__(self, name, fur_color):
            Animal.__init__(self, name)
            self._fur_color = fur_color

        def eat(self):
            print("Thanks Waff")
            return super().eat()

        def go_for_a_walk(self):
            self._fun += 3
            print(f"Waff Waff !! My fun is rising, and its: {self._fun}")

    def main():
        def create():
            new_animal = input("Dog or Turtle ??\n").lower()
            new_name = input("What his name ??\n").lower()
            new_color = input("Which color ??\n").lower()
            if new_animal == "dog":
                new_name = Dog(new_name.capitalize(), new_color.capitalize())
            elif new_animal == "turtle":
                new_name = Turtle(new_name.capitalize(), new_color.capitalize())
            return f"{new_name} created successfully"

        fluppy = Dog("Fluppy", "Brown")
        turty = Turtle("Turty", "Green")
        cls = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        running = True
        while running:
            request = 1
            # if request == 0:
            # doing = input("To create a pat press c")
            # if doing == "c":
            # print(create())
            doing = ""
            if request > 0:
                choose = input(f"Choose pet for {fluppy.name} press {fluppy.name[0].lower()}"
                               f" for {turty.name} press {turty.name[0].lower()} \n ").lower().strip()
                if choose == 'f':
                    while doing != 'c':
                        cls()
                        doing = input("For play press 'p'\nFeed your cut press 'e'"
                                      "\nGo for a walk press 'w'\nGo to toilet press press 'p'"
                                      "\nFor status press 't'\nTo change pet press 'c'").lower().strip()
                        if doing == "p":
                            fluppy.play()
                        elif doing == "e":
                            fluppy.eat()
                        elif doing == 't':
                            print(fluppy)
                        elif doing == 'w':
                            fluppy.go_for_a_walk()
                        elif doing == 'p':
                            fluppy.go_to_toilet()
                elif choose == 't':
                    while doing != 'c':
                        doing = input("For play press 'p'\nFeed your cut press 'e'\nGo to toilet press press 'p'"
                                      "\nFor status press 't'\nTo change pet press 'c'").lower().strip()
                        if doing == "p":
                            turty.play()
                        elif doing == "e":
                            turty.eat()
                        elif doing == 't':
                            print(turty)
                        elif doing == 'p':
                            turty.go_to_toilet()

    main()


if __name__ == '__main__':
    animal()
