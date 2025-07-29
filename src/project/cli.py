from typing import List
import os
import sys
import pathlib
import subprocess


import core
import utils



def input_interface():
    print(f"Welcome: {utils.username()}Date: {utils.date_bash()}")

    print(f"Enter the length of the word to guess:")
    word_length = input() 

    print(f"Enter all available letters:")
    available_letters = input()

    return (word_length, available_letters)


def output_interface(result):
    print(f"{result}")


def main():

    utils.Logs.start_of_log()

    word_length, available_letters = input_interface()

    result = core.x()

    output_interface(result)


if __name__ == "__main__":
    pass