from typing import List
from src import project


__all__: List[str] = ["main"]


def main()-> None:
    project.cli.run_cli()


if __name__ == "__main__":
    main()