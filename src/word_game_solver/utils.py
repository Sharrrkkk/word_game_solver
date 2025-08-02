import os
import pathlib
from pathlib import Path
import subprocess
import getpass
import datetime


__all__: list[str] = ["clean_console", "username", "user_datetime", "all_paths", 
                      "Logs", "UserHistory", "Parsing", "user_help", "about"]


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
    return getpass.getuser() + "\n"


def user_datetime()-> str:
    """
    """
    date: str
    time: str
    date, time = datetime.datetime.today().__str__().split()
    result: str = date + " " + ''.join(time.split(".")[0:-1])
    return result


def all_paths(get_path: str)-> Path:
    """
    """
    project_base_path: Path = pathlib.Path(__file__).resolve().parent
    config_path: Path = project_base_path / "config"
    user_history_path: Path = project_base_path / "user_history"
    logs_path: Path = project_base_path / "logs"
    scripts_path: Path = project_base_path / "scripts"
    project_data_path: Path = project_base_path / "word_files"
    help_path: Path = project_base_path / "help"
    about_path: Path = project_base_path / "about" 

    paths: dict[str, Path] = {"base":project_base_path,
             "config": config_path, 
             "history": user_history_path, 
             "logs": logs_path, 
             "scripts": scripts_path, 
             "project_data": project_data_path, 
             "help": help_path,
             "about": about_path
             }
    
    try:
        result: Path = paths[get_path]
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
            file_logs.write(f"{user_datetime()}")
            file_logs.write(f"\nStarting CLI application...\n")
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
                    record = f"{result}\n"
                case "1":
                    record = f"History viewed.\n"
                case "2":
                    record = f"History deleted.\n"
                case "3":
                    record = f"Revised Help\n"
                case "4":
                    record = f"Revised About\n"
                case "5":
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
            date, hours = user_datetime().split()
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
    def numbers(number: str)-> tuple[str, bool]:
        cache: str = number.strip(" \n")
        if len(cache) == 0:
             return (number, False)
        for digit in cache:
            if not digit.isdigit():
                return (number, False)
        return (cache, True)

    @staticmethod
    def string(string: str)-> tuple[str, bool]:
        cache: str = ''.join(string.strip(" \n").split()).lower()
        size = len(cache)
        if size == 0 or size == 1:
            return (string, False)
        for char in cache:
            if not char.isalpha():
                return (string, False)
        return (cache, True)
    

def user_help()-> None:
    help_file: Path = all_paths("help") / "help"
    subprocess.run(["nano", "-v", help_file])


def about()-> None:
    about_file: Path = all_paths("about") / "README.md"
    subprocess.run(["nano", "-v", about_file])


if __name__ == "__main__":
    pass