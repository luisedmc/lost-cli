import game as g
from blessings import Terminal


def main() -> None:
    term = Terminal()
    print(term.clear())

    # main simply runs the game
    g.run_game()
    

if __name__ == "__main__":
    main()
