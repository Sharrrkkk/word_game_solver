from typing import List, Dict, Tuple
import os
import pathlib
from pathlib import Path
import subprocess


__all__: List[str] = ["clean_console", "username", "datetime_bash", "all_paths", "Logs"]


def clean_console()-> int:
    """
    """
    result: int = 1
    if os.name == "posix":
        os.system("clear")
        result = 0
    elif os.name == "nt":
        os.system("cls")
        result = 0
    return result


def username()-> str:
    """
    """
    return subprocess.check_output("whoami", text=True)


def datetime_bash()-> str:
    """
    """
    return subprocess.check_output('echo "$(date "+%m-%d-%y %H:%M:%S")"',
                                        text=True, shell=True)


def all_paths(get_path: str)-> Path:
    """
    """
    project_base_path: Path = pathlib.Path.home() / "Desktop" / "English_word_set_generator"
    config_path: Path = project_base_path / "config"
    user_history_path: Path = project_base_path / "user_history"
    logs_path: Path = project_base_path / "logs"
    scripts_path: Path = project_base_path / "scripts"
    src_path: Path = project_base_path / "src"
    project_path: Path = src_path / "project"
    project_data_path: Path = project_path / "project_data" / "words.txt"
    help_path = project_base_path / "help"

    paths: Dict[str, Path] = {"base":project_base_path,
             "config":config_path, 
             "history":user_history_path, 
             "logs":logs_path, 
             "scripts":scripts_path, 
             "src":src_path, 
             "project":project_path, 
             "projectdata":project_data_path, 
             "help":help_path
             }
    
    try:
        result = paths[get_path]
    except:
        print(f"The key to the dic: {get_path} It is invalid.")
        raise Exception
    
    return result


class Logs:
    @staticmethod
    def start_of_log()-> None:
        """
        """
        file_logs_path: Path = all_paths("logs") / "log"
        with open(file_logs_path, "a") as file_logs:
            file_logs.write(f"{username()}")
            file_logs.write(f"{datetime_bash()}")
            file_logs.write(f"Starting CLI application...\n")
            file_logs.write(f"Console Cleaning: True\n")

    @staticmethod
    def history_log(option: str, result: str)-> None:
        """
        """
        record: str = ""
        file_logs_path: Path = all_paths("logs") / "log"
        with open(file_logs_path, "a") as file_logs:
            match option:
                case "0":
                    record = f"Revised help.\n"
                case "1":
                    record = f"{result}\n"
                case "2":
                    record = f"History viewed.\n"
                case "3":
                    record = f"History deleted.\n"
                case "4":
                    record = f"Exit...\n"
                case _:
                    record = f"Invalid option.\n"
            file_logs.write(f"{record}")

    @staticmethod
    def end_of_log()-> None:
        """
        """
        file_logs_path: Path = all_paths("logs") / "log"
        with open(file_logs_path, "a") as file_logs:
            file_logs.write(f"End CLI application...\n\n")


class UserHistory:
    @staticmethod
    def save_history(word_length: str, available_letters: str, size: int, matches: str)-> None:
        user_history_file_path: Path = all_paths("history") / "history"
        with open(user_history_file_path, "a") as file_history:
            date:str
            hours:str
            date, hours = datetime_bash().split()
            file_history.write(f"{username()}")
            file_history.write(f"Date: {date} Hours: {hours}\n")
            file_history.write(f"Desired length: {word_length}\n")
            file_history.write(f"Set of letters: {available_letters}\n")
            file_history.write(f"Matches found: {size}\n")
            file_history.write(f"List of matches: {matches}\n\n")

    @staticmethod
    def read_history()-> None:
        user_history_file_path: Path = all_paths("history") / "history"
        subprocess.run(["nano", "-v", user_history_file_path])

    @staticmethod
    def delete_history()-> None:
        user_history_file_path: Path = all_paths("history") / "history"
        with open(user_history_file_path, "w"):
            pass


class Parsing:
    @staticmethod
    def numbers(number: str)-> Tuple[str, bool]:
        cache: str = number.strip(" \n")
        if len(cache) == 0:
             return (number, False)
        for digit in cache:
            if not digit.isdigit():
                return (number, False)
        return (cache, True)

    @staticmethod
    def string(string: str)-> Tuple[str, bool]:
        cache: str = ''.join(string.strip(" \n").split()).lower()
        for char in cache:
            if not char.isalpha():
                return (string, False)
        return (cache, True)
    

def user_help()-> None:
    help_file = all_paths("help") / "help"
    subprocess.run(["nano", "-v", help_file])


if __name__ == "__main__":
    pass