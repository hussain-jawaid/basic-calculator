class BasicCalculator:
    def __init__(self):
        self.__menu()

    def __menu(self):
        while True:
            user_input = input("\nA. Addition\n"
                               "B. Subtraction\n"
                               "C. Multiplication\n"
                               "D. Division\n"
                               "E. Exit\n"
                               "Input your choice: ").lower()

            options = {
                "a": self.addition,
                "b": self.subtraction,
                "c": self.multiplication,
                "d": self.division,
                "e": self.exit_calc,
            }

            if user_input in options:
                options[user_input]()
            else:
                print("Choose option between (A,B,C,D,E)")

    def addition(self):
        print("Addition")
        first, second = self.get_numbers()
        result = first + second
        print(f"{first} + {second} = {result}")

    def subtraction(self):
        print("Subtraction")
        first, second = self.get_numbers()
        result = first - second
        print(f"{first} - {second} = {result}")

    def multiplication(self):
        print("Multiplication")
        first, second = self.get_numbers()
        result = first * second
        print(f"{first} * {second} = {result}")

    def division(self):
        print("Division")
        first, second = self.get_numbers()
        result = first / second
        print(f"{first} / {second} = {result}")

    def exit_calc(self):
        exit()

    def get_numbers(self):
        while True:
            try:
                first = int(input("Input first number: "))
                second = int(input("Input second number: "))
                return first, second
            except ValueError:
                print("Only digit allow!")


if __name__ == '__main__':
    BasicCalculator()