import random


def main():
    welcome()
    name_of_player = player_name()
    guessing_number = []
    for number in random_number():
        guessing_number.append(number)
    print(guessing_number)
    guessing(name_of_player, guessing_number)


def welcome():
    print("Hi there!\n"
          "I've generated a random 4 digit number for you.\n"
          "Let's play a bulls and cows game.\n"
                + 60 * "=")


def player_name():
    return input("What is your name? ")


def random_number():
    return random.sample(range(0, 10), 4)



def player_turn():
    turn = input("Enter a number: ")
    if len(turn) != 4:
        print("Enter only four characters!!")
        return player_turn()
    elif turn.isalpha():
        print("Enter numbers!!")
        return player_turn()
    turn_list = []
    for i in turn:
        turn_list.append(int(i))
    return turn_list


def guessing(name, guess_number):
    guesses = 0
    while True:
        index = 0
        bulls = 0
        cow = 0
        for number in player_turn():
            if number == guess_number[index]:
                bulls += 1
                index += 1
            elif number in guess_number:
                cow += 1
                index += 1
            else:
                index += 1
        guesses += 1
        if bulls == 4:
            print(f"Correct, you've guessed the right number in "
                  f"|{guesses}| guesses!\n" + 60 * "=")
            rank(guesses)
            player_leaderboard(name, guesses)
            return False
        print("|", bulls, "<< Bulls |", cow, "<< Cow |"
              , guesses, "<< Guesses |\n" + 60 * "=")


def rank(guess):
    if guess < 3:
        print("You are MASTER!!! or cheater :)")
    elif 3 <= guess <= 7:
        print("You are AMAZING player!")
    elif 7 <= guess <= 12:
        print("You are AVARAGE player!")
    else:
        print("You are not so good at this game :(")


def player_leaderboard(name, guess):
    leaderboard = open("leaderboard.txt", "r")
    line = leaderboard.readline()
    txt = line.split()
    leaderboard.close()
    if not txt or guess <= int(txt[1]):
        leaderboard = open("leaderboard.txt", "w")
        leaderboard.write(name + " " + str(guess))
        leaderboard.close()
        return print(f"NOW YOU ARE BEST PLAYER >> "
                     f"{name} << guesses: |{guess}|")
    else:
        return print(f"ALL TIME BEST PLAYER:"
                     f" >> {txt[0]} <<  GUESSES: |{txt[1]}|")


main()
