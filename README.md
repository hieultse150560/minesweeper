# Minesweeper AI
This is a project on [CS50's course Introduction to Artificial Intelligence with Python](https://www.edx.org/course/cs50s-introduction-to-artificial-intelligence-with-python) for building a AI bot for playing minesweeper automatically.
* We learn to build a data structure for storing the knowledge gained after each move and then use the knowledge base to make inference which moves is the safe move. 
* A knowledge sentence is represented by the set of cells associated with the number of mine cells amongst these cells. Based on the current knowledge, the AI can infer the new sentences from the existed ones by subtracting or reasoning based on the current structure of sentences 
* Although sometimes the AI will make a random move because of lack of knowledge, in most cases the AI can find a way to win the game just by the clue from the first move.
## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.
```bash
pip install -r requirements.txt
```
## Usage
```bash
# Make sure that all your files in one folder
python3 runner.py
```
## Contributing
I look forward to receiving comments as well as new directions for the problem.
