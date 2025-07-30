from typing import Tuple


import core
import utils


__all__ = ["run_cli"]


def input_interface()-> Tuple[int, str]:
    """
    """
    word_length: int = int(input(f"\nEnter the length of the word to guess: ")) 

    available_letters: str = input(f"Enter all available letters: ")

    return (word_length, available_letters)


def output_interface(result: int)-> str:
    matches = result if (result!='') else ('No matches')
    print(f"Number of possible words: {len(result.split())}")
    print(f"Possible words: {matches}\n")
    return matches


def run_cli()-> None:

    utils.clean_console()

    print(f"Welcome: {utils.username()}Date: {utils.date_bash()}")

    utils.Logs.start_of_log()

    while True:
        print(f"Options:")
        print(f"Generate words:.............1")
        print(f"View history:...............2")
        print(f"Delete history:.............3")
        print(f"Exit the CLI application:...4")
        option = input("select an option: ")

        matches = ""
        match option:
            case "1":
                word_length: int
                available_letters: str
                word_length, available_letters = input_interface()
                result: str = core.english_word_set_generator(word_length, available_letters)
                matches = output_interface(result)
            case "2":
                print(f"History viewed\n")
            case "3":
                print(f"History deleted\n")
            case "4":
                print(f"Exit...")
                utils.Logs.records_log(option, matches)
                break
            case _:
                print(f"Invalid option.\n")

        utils.Logs.records_log(option, matches)

    utils.Logs.end_of_log()


if __name__ == "__main__":
    pass