from typing import List, Dict, Set, Tuple
import itertools
import utils


__all__ = ["extract_transform_load", "data_analysis", "english_word_set_generator"]


def extract_transform_load(filename: str, permision: str)-> Dict[str, int]:
    filewords: Dict[str, int] = {}
    with open(filename, permision) as file:
        for line in file:
            cache: str = ''.join(sorted(line.strip(" \n")))
            if cache not in filewords:
                filewords[cache] = 0
            filewords[cache] += 1
    return filewords


def data_analysis(file: Dict[str, int], data: Tuple[int, str])-> str:
    cache: List[str] = []
    combinations: Set[str] = set()
    count: int = 0
    n: int
    word: str
    n, word = data
    for combination in itertools.combinations(word, n):
        combinations.add(''.join(sorted(combination)))
    for combination in combinations:
        count += file.get(combination, 0)
    cache.append(str(count))
    result:str = " ".join(cache)
    return result


def english_word_set_generator(n, letters):
    etl: Dict[str, int] = extract_transform_load(utils.all_paths("projectdata"), "r")
    result: str = data_analysis(etl, (n, letters))
    return result


if __name__ == "__main__":
    pass