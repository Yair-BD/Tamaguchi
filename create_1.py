from Tamaguchi.Animal import Dog, Turtle


def Create():
    def create(danimal={}):
        new_animal = input("Dog or Turtle ??\n").lower()
        new_name = input("What his name ??\n").lower()
        new_color = input("Which color ??\n").lower()
        if new_animal == "dog":
            danimal = Dog(new_name.capitalize(), new_color.capitalize())
        elif new_animal == "turtle":
            new_name = Turtle(new_name.capitalize(), new_color.capitalize())
        return f"{new_name} created successfully"

    create()


if __name__ == '__main__':
    Create()
