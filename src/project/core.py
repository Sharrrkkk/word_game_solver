from typing import List, Dict, Set, Tuple
import itertools
from . import utils
import collections
from pathlib import Path


__all__: List[str] = ["extract_transform_load", "data_analysis", "english_word_set_generator"]


def extract_transform_load(filename: Path, permision: str)-> Dict[str, List[str]]:
    filewords: Dict[str, List[str]] = collections.defaultdict(list)
    with open(filename, permision) as file:
        for line in file:
            cache: str = ''.join(sorted(line.strip(" \n")))
            word: str = line.strip(" \n")
            filewords[cache].append(word)
    return filewords


def data_analysis(file: Dict[str, List[str]], data: Tuple[int, str])-> str:
    combinations: Set[str] = set()
    n: int
    word: str
    n, word = data
    for combination in itertools.combinations(word, n):
        combinations.add(''.join(sorted(combination)))
    words_list: List[List[str]] = []
    for combination_str in combinations:
        words: List = file.get(combination_str,[])
        if len(words) > 0:
            words_list.append(words)

    cache: List[str] = [' '.join(words) for words in words_list]
    result:str = ' '.join(sorted(set(cache)))
    return result


def english_word_set_generator(n: int, letters: str)-> str:
    etl: Dict[str, List[str]] = extract_transform_load(utils.all_paths("projectdata"), "r")
    result: str = data_analysis(etl, (n, letters))
    return result


if __name__ == "__main__":
    pass