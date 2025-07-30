from typing import Tuple, List


import core
import utils


__all__: List[str] = ["run_cli"]


def input_interface()-> Tuple[str, str]:
    """
    """
    word_length: str = input(f"\nEnter the length of the word to guess: ")

    available_letters: str = input(f"Enter all available letters: ")

    return (word_length, available_letters)


def output_interface(result: int)-> Tuple[str, int]:
    size: int = len(result.split())
    matches: str = result if (result!='') else ('No matches')
    print(f"Number of possible words: {size}")
    print(f"Possible words: {matches}\n")
    return (size, matches)




def generate_words()-> str:
    word_length: str
    available_letters: str
    word_length, available_letters = input_interface()

    parsing_word_length: int | str
    status_length: bool
    parsing_word_length, status_length = utils.Parsing.numbers(word_length)

    parsing_available_letters: str
    status_letters: bool
    parsing_available_letters, status_letters = utils.Parsing.string(available_letters)

    matches: str = ""
    status: List[bool] = [status_length, status_letters]
    if sum(status) == 2:
        result: str = core.english_word_set_generator(parsing_word_length, parsing_available_letters)
        size: int
        matches: str
        size, matches = output_interface(result)
        utils.UserHistory.save_history(word_length, available_letters, size, matches)
    else:
        incorrect_entries: str = "Both entries are incorrect, please read the help."
        incorrect_length: str = "The length entered is incorrect, please read the help."
        incorrect_letters: str = "the letter set is incorrect, please read the help."
        matches: str = f"{incorrect_entries if (sum(status)==0) else(incorrect_length) if(status[0]==0) else(incorrect_letters)}"
        print(matches + "\n")

    return matches


def run_cli()-> None:

    utils.clean_console()

    date: str
    hours: str
    date, hours = utils.datetime_bash().split()
    print(f"Welcome: {utils.username()}Date: {date} Hours: {hours}\n")

    utils.Logs.start_of_log()

    while True:
        print(f"Options:")
        print(f"Help:.......................0")
        print(f"Generate words:.............1")
        print(f"View history:...............2")
        print(f"Delete history:.............3")
        print(f"Exit the CLI application:...4")
        option: str = input("Select an option: ")

        matches: str = ""
        match option:
            case "0":
                utils.user_help()
                print(f"Revised help\n")
            case "1":
                matches = generate_words()
            case "2":
                utils.UserHistory.read_history()
                print(f"History viewed\n")
            case "3":
                utils.UserHistory.delete_history()
                print(f"History deleted\n")
            case "4":
                print(f"Exit...")
                utils.Logs.history_log(option, matches)
                break
            case _:
                print(f"Invalid option.\n")

        utils.Logs.history_log(option, matches)

    utils.Logs.end_of_log()


if __name__ == "__main__":
    pass