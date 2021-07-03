from clear_1 import Clear
from objects import *


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

    def exercise(self):
        return "I feel so strong now !!"

    def print_hunger(self):
        print(self._hunger)

    def __str__(self):
        return f"My name is {self.name} and i love u ^_^ \n" \
               f"my hunger is {self._hunger} \nand my fun is {self._fun} ^_^ "


class Turtle(Animal):
    def __init__(self, name, color, armor=0, home=[]):
        Animal.__init__(self, name)
        self.t_color = color
        self.p = "turtle"
        self.p_armor = armor
        self.e_home = home

    def gifting(self):
        gift = input("What do you give mee ? \n")
        self.e_home.append(gift)
        self._fun += 1
        return print("Ho i'm appreciate that :)")

    def eat(self):
        print("Ho good hasa for a good filling")
        return super(Turtle, self).eat()

    def __str__(self):
        if self.e_home == "":
            return super(Turtle, self).__str__()
        else:
            return super(Turtle,
                         self).__str__() + f"\nand i am happy with the home tools you gave me :{', '.join(self.e_home)}"


class Dog(Animal):
    def __init__(self, name, fur_color):
        Animal.__init__(self, name)
        self._fur_color = fur_color
        self.p = "dog"

    def eat(self):
        print("Thanks Waff")
        return super().eat()

    def go_for_a_walk(self):
        self._fun += 3
        print(f"Waff Waff !! My fun is rising")


def create(number_of_try=0):
    new_animal = input("Dog or Turtle ??\n").lower()
    new_name = input("Give him a name\n").lower()
    new_color = input("Which color will be the best ??\n").lower()
    if new_animal == "dog":
        a_d[a_l[number_of_try]] = Dog(new_name.capitalize(), new_color.capitalize())
        print(f"{new_name} created successfully")
        return a_d[a_l[number_of_try]], new_name[0]
    elif new_animal == "turtle":
        a_d[a_l[number_of_try]] = Turtle(new_name.capitalize(), new_color.capitalize())
        print(f"{new_name} created successfully")
        return a_d[a_l[number_of_try]], new_name[0]


def main():
    final_animal = ""
    request_to_create = 0
    all_letters = []
    system_names = []
    running = True
    open_create = True
    while running:
        doing = ""
        if open_create:
            s_n, first_letter = create(request_to_create)
            all_letters.append(first_letter)
            system_names.append(s_n)
            request_to_create += 1
            open_create = False
        elif not open_create:
            ziping_names_letters = zip(system_names, all_letters)
            for nam, letter in ziping_names_letters:
                print(f"for {nam.name} press {letter}")
            choose = input("To create another pet press '+'").lower().strip()
            Clear()
            if choose == "+":
                open_create = True
                continue
            elif choose in all_letters:
                final_animal = system_names[all_letters.index(choose)]
                print(final_animal)
                # print(all_letters.index(choose))
                if final_animal.p == "dog":
                    while doing != 'c':
                        Clear()
                        doing = input("For play press 'p'\nFeed your cut press 'e'"
                                      "\nGo for a walk press 'w'\nGo to toilet press press 'p'"
                                      "\nFor status press 't'\nTo change pet press 'c'").lower().strip()
                        Clear()
                        if doing == "p":
                            final_animal.play()
                        elif doing == "e":
                            final_animal.eat()
                        elif doing == 't':
                            print(final_animal)
                        elif doing == 'w':
                            final_animal.go_for_a_walk()
                        elif doing == 'p':
                            final_animal.go_to_toilet()
                elif final_animal.p == 'turtle':
                    while doing != 'c':
                        Clear()
                        doing = input(f"For play press 'p'\nFeed your cut press 'e'"
                                      f"\nGiving for {final_animal.name} a home tool press 'g' \nGo to toilet press press 'p'"
                                      "\nFor status press 't'\nTo change pet press 'c'").lower().strip()
                        Clear()
                        if doing == "p":
                            final_animal.play()
                        elif doing == "e":
                            final_animal.eat()
                        elif doing == "g":
                            final_animal.gifting()
                        elif doing == 't':
                            print(final_animal)
                        elif final_animal == 'p':
                            final_animal.go_to_toilet()


main()
