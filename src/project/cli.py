from typing import Tuple, List


import core
import utils


__all__: List[str] = ["run_cli"]


def input_interface()-> Tuple[int, str]:
    """
    """
    word_length: int = int(input(f"\nEnter the length of the word to guess: ")) 

    available_letters: str = input(f"Enter all available letters: ")

    return (word_length, available_letters)


def output_interface(result: int)-> Tuple[str, int]:
    size = len(result.split())
    matches: str = result if (result!='') else ('No matches')
    print(f"Number of possible words: {size}")
    print(f"Possible words: {matches}\n")
    return (size, matches)


def run_cli()-> None:

    utils.clean_console()

    date, hours = utils.datetime_bash().split()
    print(f"Welcome: {utils.username()}Date: {date} Hours: {hours}\n")

    utils.Logs.start_of_log()

    while True:
        print(f"Options:")
        print(f"Generate words:.............1")
        print(f"View history:...............2")
        print(f"Delete history:.............3")
        print(f"Exit the CLI application:...4")
        option: str = input("Select an option: ")

        matches: str = ""
        match option:
            case "1":
                word_length: int
                available_letters: str
                word_length, available_letters = input_interface()
                result: str = core.english_word_set_generator(word_length, available_letters)
                size: int
                matches: str
                size, matches = output_interface(result)
                utils.User_History.save_history(word_length, available_letters, size, matches)
            case "2":
                utils.User_History.read_history()
                print(f"History viewed\n")
            case "3":
                utils.User_History.delete_history()
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