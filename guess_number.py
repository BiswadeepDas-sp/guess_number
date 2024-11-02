import random

class Number:
    def generate(self):
        return random.randint(1, 100)

class User:
    def get_guess(self):
        while True:
            try:
                guess = int(input('Guess a number between 1 and 100: '))
                if 1 <= guess <= 100:
                    return guess
                else:
                    print('Please enter a number between 1 and 100.')
            except ValueError:
                print('Invalid input. Please enter an integer.')

    def get_choice(self):
        while True:
            try:
                choice = int(input('Continue (0) or Exit (1): '))
                if choice in (0, 1):
                    return choice
                else:
                    print('Please enter 0 or 1.')
            except ValueError:
                print('Invalid input. Please enter 0 or 1.')

class Game:
    def __init__(self):
        self.score = 0
        self.guesses_left = 5
        self.cheat = False

    def calculate_score(self, guess, number):
        if not self.cheat and self.guesses_left > 0:
            return round(100 - (abs(guess - number) / number * 100), 0)
        return 0

    def game_play(self):
        number = Number().generate()
        user = User()
        self.guesses_left = 5
        self.cheat = False
        win = False

        print(f"The number is {number}")  # For testing; consider removing this line in production

        while self.guesses_left > 0 and not win:
            guess = user.get_guess()

            if guess == 999:
                print(f"The number is {number}")
                self.cheat = True
                continue

            self.guesses_left -= 1

            if guess == number:
                print(f"\nYou have won in {5 - self.guesses_left} guess{'es' if 5 - self.guesses_left > 1 else ''}!")
                win = True
            else:
                print("Wrong guess, try again!")
                if self.guesses_left > 0:
                    print(f"You have {self.guesses_left} guesses left.")

            self.score += self.calculate_score(guess, number)
            print(f"Score: {self.score}")
            print("*" * 30)

        if not win:
            print("\nToo many guesses, better luck next time!")
            print(f"The number was {number}")
            print("*" * 30)

        if self.cheat:
            print("*" * 30)
            print("HMMMM. Okay!")

        if user.get_choice() == 0:
            self.game_play()
        else:
            exit()

# Start the game
game = Game()
game.game_play()
