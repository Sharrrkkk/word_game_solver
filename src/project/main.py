from typing import List
import cli


__all__: List[str] = ["main"]


def main()-> None:
    cli.run_cli()


if __name__ == "__main__":
    main()