the_board = {"TOP_LEFT": " ", "TOP_MID": " ", "TOP_RIGHT": " ",
             "MID_LEFT": " ", "MID_MID": " ", "MID_RIGHT": " ",
             "BOT_LEFT": " ", "BOT_MID": " ", "BOT_RIGHT": " "}


def print_board():
    print(the_board["TOP_LEFT"] + "|" + the_board["TOP_MID"] + "|" + the_board["TOP_RIGHT"])
    print("-+-+-")
    print(the_board["MID_LEFT"] + "|" + the_board["MID_MID"] + "|" + the_board["MID_RIGHT"])
    print("-+-+-")
    print(the_board["BOT_LEFT"] + "|" + the_board["BOT_MID"] + "|" + the_board["BOT_RIGHT"])


def start_game():
    print_board()


if __name__ == '__main__':
    start_game()
