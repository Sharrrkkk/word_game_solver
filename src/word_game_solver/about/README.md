# **Anagram Generator.**

Generate valid English word sets based on a specified word length and a set of input characters using anagrams and a file with English words.

---

## **Features:**

- Input a desired word length (e.g., `5`)
- Provide a set of characters (e.g., `"nyogbsfo"`)
- Generate all valid English words (e.g., `bongo`, `bongs`, `boons`, etc.)
- Uses an anagram-solving algorithm
- Relies on a plain English word list (`words.txt`)

---

## **Usage:**

Run the following command from your terminal (Unix-like systems (Mac, Linux, etc.):

```bash
python3 English_word_generator.py
```

A simple interactive menu will appear:

Generate words

View history

Delete history

Exit application

When generating words, simply enter the word length and a character set.

The CLI will return all valid matches from words.txt.

The history consists of all the word length and character set entries entered as input and their corresponding output. Across all sessions, it is automatically saved and can also be deleted.

---

## **Project structure:**

.
├── LICENSE
├── README.md
├── config
│ └── config
├── data
│ └── data
├── logs
│ └── log
├── pyproject.toml
├── requirements.txt
├── scripts
│ └── automation.py
├── setup.py
├── src
│ └── project
│ ├── __init__.py
│ ├── cli.py
│ ├── core.py
│ ├── main.py
│ ├── project_data
│ │ └── words.txt
│ └── utils.py
└── tests 
└── tests.py

---

## **Visual example of the CLI application in action:**

Welcome: user
Date: 07-29-25 22:01:06

Options:
Generate words:..........1
View history:...............2
Delete history:..........3
Exit the CLI application:...4
Select an option: 1

Enter the length of the word to guess: 5
Enter all available letters: nyogbsfo
Number of possible words: 6
Possible words: bongo bongs boons goofs goofy goons

Options:
Generate words:.............1
View history:...............2
Delete history:.............3
Exit the CLI application:...4
Select an option: 4
Exit...

---

## **License:**
This project is licensed under the MIT License.

---

## **Notes:**

You can replace words.txt with a word list of your choice. The program filters each line to remove special characters, digits, and spaces, and it normalizes all text to lowercase. Currently, it only supports plain alphabetic characters (A–Z/a–z), without accents or symbols.

This project is 100% educational.

This project is geared toward Linux/Unix systems. I'll be adding a Windows-compatible version soon.

---