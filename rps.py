from random import choice

OPTIONS = ("rock", "paper", "scissors")


def get_computer_choice():
    computer_choice = choice(OPTIONS)
    return computer_choice


def get_player_choice():
    while True:
        player_choice = input(f"Enter a choice {OPTIONS} : ").lower()
        if player_choice in OPTIONS:
            return player_choice
        print("Invalid choice. Please choose again.")


def rock_paper_scissors(computer: str, player: str):
    if computer == player:
        return "tie"
    elif player == "rock":
        if computer == "scissors":
            return "You smashed the scissors :)"
        else:
            return "Your rock got covered :("
    elif player == "paper":
        if computer == "scissors":
            return "You got cut :("
        else:
            return "You covered the rock :)"
    elif player == "scissors":
        if computer == "rock":
            return "You got smashed ;("
        else:
            return "You cut him :)"


def main():
    c_choice = get_computer_choice()
    p_choice = get_player_choice()
    print(f"Your choice --> {p_choice} , computer's choice --> {c_choice}.")
    result = rock_paper_scissors(c_choice, p_choice)
    print(result)

if __name__ == '__main__':
    main()
