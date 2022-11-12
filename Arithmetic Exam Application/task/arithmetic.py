import random


class Arithmetic:
    intro = """
    Which level do you want? Enter a number:
    1 - simple operations with numbers 2-9
    2 - integral squares of 11-29
    """

    def __init__(self):
        self.value_1 = None
        self.value_2 = None
        self.operand = None
        self.operand_list = None
        self.value = None
        self.result = None
        self.mark = None
        self.level = None
        self.level_description = None

    def addition(self):
        return self.value_1 + self.value_2

    def subtraction(self):
        return self.value_1 - self.value_2

    def multiplication(self):
        return self.value_1 * self.value_2

    def operation(self):
        if self.operand == "+":
            return self.addition()
        elif self.operand == "-":
            return self.subtraction()
        elif self.operand == "*":
            return self.multiplication()

    def random_pickup(self):
        self.value_1 = random.randint(2, 9)
        self.value_2 = random.randint(2, 9)
        self.operand_list = ["+", "-", "*"]
        self.operand = random.choice(self.operand_list)
        self.value = random.randint(11, 29)

    def simple_try(self):
        print(f"{self.value_1} {self.operand} {self.value_2}")

    def number(self):
        print(self.value)

    def squares_operation(self):
        return self.value ** 2

    def simple_operation(self, random_pickup, simple_try, operation):
        n = 0
        step = 0
        while step < 5:
            random_pickup()
            while True:
                try:
                    simple_try()
                    if int(input()) == operation():
                        print("Right!")
                        n += 1
                        step += 1
                    else:
                        print("Wrong!")
                        step += 1
                    break
                except ValueError:
                    print("Incorrect format.")

        self.mark = f"{n}/5"
        self.result = f"Your mark is {self.mark}.Would you like to save the result? Enter yes or no."
        print(self.result)

    def save_result(self):
        answer = input()
        if answer in ("Yes", "YES", "y", "yes"):
            print("What is your name?")
            name = input()
            with open("results.txt", "a") as note:
                note.write(f"{name}: {self.mark} in level {self.level} ({self.level_description}).")
            print('The results are saved in "results.txt".')
        else:
            pass

    def calculation(self):
        print(self.intro)
        self.level = int(input())
        if self.level == 1:
            self.level_description = "simple operations with numbers 2-9"
            self.simple_operation(self.random_pickup, self.simple_try, self.operation)
        elif self.level == 2:
            self.level_description = "integral squares of 11-29"
            self.simple_operation(self.random_pickup, self.number, self.squares_operation)
        self.save_result()


arithmetic_exam = Arithmetic()
arithmetic_exam.calculation()
