from src import word_game_solver


__all__: list[str] = ["main"]


def main()-> None:
    word_game_solver.cli.run_cli()


if __name__ == "__main__":
    main()