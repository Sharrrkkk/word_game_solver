from . import core
from . import utils


__all__: list[str] = ["run_cli"]


class AnagramGenerator:
    @staticmethod
    def input_data()-> tuple[str, str]:
        print(f"\nAnagram Generator")
        word_length: str = input(f"Enter the length of the word to guess: ")
        available_letters: str = input(f"Enter all available letters: ")
        return (word_length, available_letters)

    @staticmethod
    def anagram_generator(word_length: str, available_letters: str)-> tuple[bool, str]:
        parsing_word_length: str
        status_length: bool
        parsing_word_length, status_length = utils.Parsing.numbers(word_length)

        parsing_available_letters: str
        status_letters: bool
        parsing_available_letters, status_letters = utils.Parsing.string(available_letters)

        status: list[bool] = [status_length, status_letters]
        matches: str
        if sum(status) == 2:
            int_word_length = int(parsing_word_length)
            return (True, core.anagram_generator(int_word_length, parsing_available_letters)) 
        else:
            incorrect_entries: str = "Both entries are incorrect, please read the help."
            incorrect_length: str = "The length entered is incorrect, please read the help."
            incorrect_letters: str = "the letter set is incorrect, please read the help."
            matches = f"{incorrect_entries if (sum(status)==0) else(incorrect_length) if(status[0]==0) else(incorrect_letters)}"
            return (False, matches)
    
    @staticmethod
    def output_data(length: str, letters: str, status: bool, result: str)-> None:
        if status:
            size: int = len(result.split())
            matches: str = result if (result!='') else ('No matches')
            print(f"Number of possible words: {size}")
            print(f"Possible words: {matches}")
            utils.UserHistory.save_history(length, letters, size, matches)
            utils.Logs.history_log("0", matches)
        else:
            print(result)
            utils.Logs.history_log("0", result)


def word_game_solver()-> None:
    while True:
        print(f"\nWord Game Solver")
        print(f"Games:")
        print(f"Anagram Generator...1")
        print(f"Exit................2")
        game: str = input(f"Select an Game: ")

        match game:
            case '1':
                word_length: str
                available_letters: str
                word_length, available_letters = AnagramGenerator.input_data()
                status: bool
                result: str
                status, result = AnagramGenerator.anagram_generator(word_length, available_letters)
                AnagramGenerator.output_data(word_length, available_letters, status, result)
            case '2':
                print("exit..." + "\n")
                utils.Logs.history_log("0", "exit...")
                break
            case _:                
                print("Invalid game option")
                utils.Logs.history_log("0", "Invalid game option")
        

def run_cli()-> None:

    utils.clean_console()

    print(f"Word Game Solver")

    date: str
    hours: str
    date, hours = utils.user_datetime().split()
    print(f"Welcome: {utils.username()}Date: {date} Hours: {hours}\n")

    utils.Logs.start_of_log()

    while True:
        print(f"Word Game Solver")
        print(f"Options:")
        print(f"Select game:................0")
        print(f"View history:...............1")
        print(f"Delete history:.............2")
        print(f"Help:.......................3")
        print(f"About:......................4")
        print(f"Exit the CLI application:...5")
        option: str = input("Select an option: ")

        matches: str = ""
        match option:
            case "0":
                word_game_solver()
                continue
            case "1":
                utils.UserHistory.read_history()
                print(f"History viewed\n")
            case "2":
                utils.UserHistory.delete_history()
                print(f"History deleted\n")
            case "3":
                utils.user_help()
                print(f"Revised Help\n")
            case "4":
                utils.about()
                print(f"Revised About\n")
            case "5":
                print(f"Exit...")
                utils.Logs.history_log(option, matches)
                break
            case _:
                print(f"Invalid option.\n")

        utils.Logs.history_log(option, matches)

    utils.Logs.end_of_log()


if __name__ == "__main__":
    run_cli()