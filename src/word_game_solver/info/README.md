# **Word Game Solver.**

Solve several word puzzles.
Currently, only the Anagram Generator is implemented.
This consists of searching for all possible words from a desired length and a set of letters. The possible words are stored in an English word file, and an anagram-based algorithm is used.
---

## **Features:**

### Anagram generator
- Input a desired word length (e.g., `5`)
- Provide a set of characters (e.g., `"nyogbsfo"`)
- Generate all valid English words (e.g., `bongo`, `bongs`, `boons`, etc.)
- Uses an anagram-solving algorithm
- Relies on a plain English word list (`words.txt`)

---

## **Usage:**

Run the following command from your terminal (Unix-like systems (Mac, Linux, etc.):
If installed manually, or with a GitHub clone, it can be started with the command.
```bash
python3 main.py
```
If installed as a package, you can simply run the anagrams command
```bash
anagrams
```

A simple interactive menu will appear:

Select Game

View history

Delete history

Help

About

Exit application

At the moment only the Anagram Generator game is available.
When generating words, simply enter the word length and a character set.
The CLI will return all valid matches from words.txt.
The history consists of all the word length and character set entries entered as input and their corresponding output. Across all sessions, it is automatically saved and can also be deleted.

---

## **Project structure:**

.
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
├── scripts
│   └── automation.py
├── src
│   └── word_game_solver
│       ├── __init__.py
│       ├── about
│       │   ├── LICENSE
│       │   └── README.md
│       ├── cli.py
│       ├── config
│       │   └── config
│       ├── core.py
│       ├── help
│       │   └── help
│       ├── logs
│       │   └── log
│       ├── scripts
│       │   └── script.py
│       ├── user_history
│       │   └── history
│       ├── utils.py
│       └── word_files
│           └── english_words.txt
├── tests
│   └── tests.py

---

## **Visual example of the CLI application in action:**

Word Game Solver
Welcome: user
Date: 2025-08-02 Hours: 18:48:23

Word Game Solver
Options:
Select game:................0
View history:...............1
Delete history:.............2
Help:.......................3
About:......................4
Exit the CLI application:...5
Select an option: 0

Word Game Solver
Games:
Anagram Generator...1
Exit................2
Select an Game: 1

Anagram Generator
Enter the length of the word to guess: 5
Enter all available letters: dhsfutsomfahd
Number of possible words: 39
Possible words: atoms moats autos dados datum doffs dusts studs fasts foams hafts shaft hosts shots huffs masts moths mouth muffs musts smuts oaths ousts shads shahs shams smash shout south thous shush shuts sodas sofas staff stash stuff thuds toads

---

## **License:**
This project is licensed under the MIT License.

---

## **Notes:**

You can replace words.txt with a word list of your choice. The program filters each line to remove special characters, digits, and spaces, and it normalizes all text to lowercase. Currently, it only supports plain alphabetic characters (A–Z/a–z), without accents or symbols.

This project is 100% educational.

This project is geared toward Linux/Unix systems. I'll be adding a Windows-compatible version soon.

---