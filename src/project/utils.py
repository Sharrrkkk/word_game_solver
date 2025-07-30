from typing import List, Dict
import os
import pathlib
from pathlib import Path
import subprocess


__all__: List[str] = ["clean_console", "username_linux", "date_bash", "all_paths", "Logs"]


def clean_console()-> int:
    """
    """
    result = 1
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

    paths: Dict[str, Path] = {"base":project_base_path,
             "config":config_path, 
             "history":user_history_path, 
             "logs":logs_path, 
             "scripts":scripts_path, 
             "src":src_path, 
             "project":project_path, 
             "projectdata":project_data_path, 
             }
    
    return paths.get(get_path, "Incorrect path")


class Logs:
    def __init__():
        pass
    
    @staticmethod
    def start_of_log():
        """
        """
        file_logs_path = all_paths("logs") / "log"
        with open(file_logs_path, "a") as file_logs:
            file_logs.write(f"{username()}")
            file_logs.write(f"{datetime_bash()}")
            file_logs.write(f"Starting CLI application...\n")
            file_logs.write(f"Console Cleaning: True\n")

    @staticmethod
    def records_log(option: int, result: str):
        """
        """
        records = ""
        file_logs_path = all_paths("logs") / "log"
        with open(file_logs_path, "a") as file_logs:
            match option:
                case "1":
                    records = f"{result}\n"
                case "2":
                    records = f"History viewed.\n"
                case "3":
                    records = f"History deleted.\n"
                case "4":
                    records = f"Exit...\n"
                case _:
                    records = f"Invalid option.\n"
            file_logs.write(f"{records}")

    @staticmethod
    def end_of_log():
        """
        """
        file_logs_path = all_paths("logs") / "log"
        with open(file_logs_path, "a") as file_logs:
            file_logs.write(f"End CLI application...\n\n")



class User_History:
    @staticmethod
    def save_history(word_length, available_letters, size, matches):
        user_history_file_path = all_paths("history") / "history"
        with open(user_history_file_path, "a") as file_history:
            date, hours = datetime_bash().split()
            file_history.write(f"{username()}")
            file_history.write(f"Date: {date} Hours: {hours}\n")
            file_history.write(f"Desired length: {word_length}\n")
            file_history.write(f"Set of letters: {available_letters}\n")
            file_history.write(f"Matches found: {size}\n")
            file_history.write(f"List of matches: {matches}\n\n")

    @staticmethod
    def read_history():
        user_history_file_path = all_paths("history") / "history"
        subprocess.run(["nano", user_history_file_path])

    @staticmethod
    def delete_history():
        user_history_file_path = all_paths("history") / "history"
        with open(user_history_file_path, "w") as file_history:
            pass


if __name__ == "__main__":
    pass