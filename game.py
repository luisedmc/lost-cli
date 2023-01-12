from colorama import Fore


def welcome_screen() -> None:
    """
    welcome_screen simply shows the welcome screen of the game to the user.
    """
    print(Fore.RED +
        "                                   D U N G E O N"
    )

    print(Fore.GREEN +
        """
        Game Description
        """
    )


def run_game() -> None:
    welcome_screen()

    input(
        """
        I can see you made a good decision!
        Hit the ENTER key to start the game.
        """
    )
    explore_labyrinth()


def explore_labyrinth() -> None:
    while True:
        player_input = input(Fore.LIGHTCYAN_EX + "-> ").lower().strip()

        # Get the option selected from the User
        if player_input == "exit":
            # TODO: Add a confirmation message
            confirmation_exit("exit")

            play_again()

        elif player_input == "help":
            show_help()

        else:
            print(Fore.YELLOW +
        """
        I don't think I understand what you mean...
        Maybe you could type 'help' and see what happens?
        """
        )


def show_help() -> None:
    print(Fore.YELLOW +
        """
        If you need help, you have a few options:

        Player Options:
        - w/s/d/a to move Up/Down/Right/Left
        - map to show the map
        - look to look around your current position
        - inventory to show your inventory
        - equip <item> to equip an item from your inventory
        - unequip <item> to unequip an item from your inventory
        - examine <item> to examine an item from your inventory
        - use <item> to use an item from your inventory
        - take <item> to take an item from the ground
        - drop <item> to drop an item from your inventory

        Game Options:
        - 'exit' to leave the game
        - 'help' to show this message
        
        """
    )


def play_again() -> None:
    answer = input(Fore.YELLOW +
        """
        So...
        You want to play again?
        Just answer with a simple 'yes' or 'no' and I will know what to do...
-> """
    ).lower().strip()

    while answer not in ["yes", "no"]:
        answer = input(Fore.YELLOW +
        """
        I don't think I understand what you mean...
        Maybe you could type 'yes' or 'no'?
-> """
        )

    if answer == "yes":
        run_game()
        
    elif answer == "no":
        print(Fore.RED +
        """
        So you choose to leave...
        Another soul lost in the labyrinth.
        """
        )
        exit(0)


def confirmation_exit(answer: str):
    answer = input(Fore.YELLOW +
        f"""
        Are you sure you want to {answer}?
        You can answer if a simple 'yes' or 'no'.
        It's ok, you can go back to the game if you type 'no'. 
-> """
    ).lower().strip()