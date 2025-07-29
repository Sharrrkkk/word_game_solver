import os


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


if __name__ == "__main__":
    pass