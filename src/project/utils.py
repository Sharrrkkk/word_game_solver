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


def date_bash()-> str:
    """
    """
    return subprocess.check_output('echo "$(date "+%m-%d-%y %H:%M:%S")"',
                                        text=True, shell=True)


def all_paths(get_path: str)-> Path:
    """
    """
    project_base_path: Path = pathlib.Path.home() / "Desktop" / "English_word_set_generator"
    config_path: Path = project_base_path / "config"
    data_path: Path = project_base_path / "data"
    logs_path: Path = project_base_path / "logs"
    scripts_path: Path = project_base_path / "scripts"
    src_path: Path = project_base_path / "src"
    project_path: Path = src_path / "project"
    project_data_path: Path = project_path / "project_data" / "words.txt"

    paths: Dict[str, Path] = {"base":project_base_path,
             "config":config_path, 
             "data":data_path, 
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

    def start_of_log():
        """
        """
        file_logs_path = all_paths("logs") / "logs"
        with open(file_logs_path, "w") as file_logs:
            file_logs.write(f"{username()} {date_bash()}")
            file_logs.write(f"Starting CLI application...\n")
            file_logs.write(f"Console Cleaning: {True if (clean_console() == 0) else False}\n")


if __name__ == "__main__":
    pass