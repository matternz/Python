#Matthew Norris
#random number guess game
import random


def select_difficulty():
    """
    returns how many turns a player has to guess a number
    :return:
    """
    while True:
        try:
            print("Select difficulty level 1 - 3:")
            print("1 - EASY (7 Chances)")
            print("2 - MEDIUM (6 Chances)")
            print("3 - HARD (5 Chances)")
            difficulty_level = int(input())
        except ValueError:
            print("You must select a number")
            continue
        if not 0 <= difficulty_level <= 4:
            print("You must select a number between 1 and 3")
        else:
            if difficulty_level == 1:
                print("You have selected EASY")
                return 7
            elif difficulty_level == 2:
                print("You have selected MEDIUM")
                return 6
            elif difficulty_level == 3:
                print("You have selected HARD")
                return 5


def random_number_lower_range():
    """
    returns the lower limit of the random number
    :return:
    """
    while True:
        try:
            print("Select the lower range of your random number")
            lower_limit = int(input())
        except ValueError:
            print("You must select a number")
            continue
        return lower_limit


def random_number_upper_range(lower_limit):
    """
    returns the upper limit of the random number
    :param lower_limit:
    :return:
    """
    while True:
        try:
            print("Select the upper range of your random number")
            upper_limit = int(input())
        except ValueError:
            print("You must select a number")
            continue
        if upper_limit <= lower_limit:
            print("You must select a number that is higher than " + str(lower_limit))
            continue
        return upper_limit


def generate_random_number(lower, upper):
    """
    generates a random number between lower and upper
    :param lower:
    :param upper:
    :return:
    """
    return random.randint(lower, upper)


def evaluate_guess(lower, upper, rand, guess):
    """
    evalulates if the guess is correct, out of range and whether they need to go higher or lower
    :param lower:
    :param upper:
    :param rand:
    :param guess:
    :return:
    """
    if guess == rand:
        return True
    elif not lower < guess < upper:
        print("The range is " + str(lower) + " to " + str(upper))
        return False
    else:
        print("You need to guess {}.".format("lower" if guess > rand else "higher"))


def play_game(lower, upper, rand, attempts):
    """
    runs the game and handles whether you won or not in a certain number of attempts
    :param lower:
    :param upper:
    :param rand:
    :param attempts
    :return:
    """
    print("A random number has being generated between " + str(lower) + " and " + str(upper))
    count = 0
    while True:
        try:
            print("guess the number :  ")
            guess = int(input())
            correct = evaluate_guess(lower, upper, rand, guess)
            if correct:
                print("Congratulations you won!")
                break
            elif count >= attempts:
                print("You ran out of attempts")
                print("The number was " + str(rand))
                break
            count += 1
        except ValueError:
            print("You must select a number")
            continue


def start_game():
    """
    used to start the game
    :return:
    """
    print("Hello this is a game where you try guess the correct number")
    lower = random_number_lower_range()
    upper = random_number_upper_range(lower)
    rand = generate_random_number(lower, upper)
    play_game(lower, upper, rand, select_difficulty())


if __name__ == '__main__':
    start_game()
