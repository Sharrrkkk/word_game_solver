from typing import List
import os
import sys
import pathlib
import subprocess


import core
import utils


def all_paths(get_path):
    project_base_path = pathlib.Path.home() / "Desktop" / "English_word_set_generator"
    config_path = project_base_path / "config"
    data_path = project_base_path / "data"
    logs_path = project_base_path / "logs"
    scripts_path = project_base_path / "scripts"
    src_path = project_base_path / "src"
    project_path = src_path / "project"
    project_data_path = project_path / "project_data"

    paths = {"base":project_base_path,
             "config":config_path, 
             "data":data_path, 
             "logs":logs_path, 
             "scripts":scripts_path, 
             "src":src_path, 
             "project":project_path, 
             "projectdata":project_data_path, 
             }
    
    return paths.get(get_path, "Incorrect path")



def main():
    logs = all_paths("logs") / "logs"
    with open(logs, "a") as file_logs:
        data = subprocess.check_output("echo '$(whoami) $(date '+%m-%d-%y %H:%M:%S')'",
                                        text=True, shell=True)
        file_logs.write(f"{data}")
        file_logs.write(f"Starting CLI application...")
        file_logs.write(f"Console Cleaning: {True if (utils.clean_console() == 0) else False}")


if __name__ == "__main__":
    pass