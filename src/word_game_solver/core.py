import itertools
from . import utils
import collections
from pathlib import Path


__all__: list[str] = ["extract_transform_load", "data_analysis", "anagram_generator"]


def extract_transform_load(filename: Path, permision: str)-> dict[str, list[str]]:
    filewords: dict[str, list[str]] = collections.defaultdict(list)
    with open(filename, permision) as file:
        for line in file:
            cache: str = ''.join(sorted(line.strip(" \n")))
            word: str = line.strip(" \n")
            filewords[cache].append(word)
    return filewords


def data_analysis(file: dict[str, list[str]], data: tuple[int, str])-> str:
    combinations: set[str] = set()
    n: int
    word: str
    n, word = data
    for combination in itertools.combinations(word, n):
        combinations.add(''.join(sorted(combination)))
    words_list: list[list[str]] = []
    for combination_str in combinations:
        if file[combination_str]:
            words: list[str] = file[combination_str]
            words_list.append(words)

    cache: list[str] = [' '.join(words) for words in words_list]
    result:str = ' '.join(sorted(set(cache)))
    return result


def anagram_generator(n: int, letters: str)-> str:
    etl: dict[str, list[str]] = extract_transform_load(utils.all_paths("project_data") / "english_words.txt", "r")
    result: str = data_analysis(etl, (n, letters))
    return result


if __name__ == "__main__":
    pass