from typing import List, Tuple


import core
import utils


def input_interface()-> Tuple[int, str]:
    """
    """
    print(f"Welcome: {utils.username()}Date: {utils.date_bash()}")

    word_length: int = int(input(f"Enter the length of the word to guess: ")) 

    available_letters: str = input(f"Enter all available letters: ")

    return (word_length, available_letters)


def output_interface(result: int)-> None:
    print(f"Number of possible words: {result}")


def main()-> None:

    utils.Logs.start_of_log()

    word_length: int
    available_letters: str
    word_length, available_letters = input_interface()

    result: str = core.english_word_set_generator(word_length, available_letters)

    output_interface(result)


if __name__ == "__main__":
    pass