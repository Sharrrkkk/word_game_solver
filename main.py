from typing import List
from src import anagram_generator


__all__: List[str] = ["main"]


def main()-> None:
    anagram_generator.cli.run_cli()


if __name__ == "__main__":
    main()