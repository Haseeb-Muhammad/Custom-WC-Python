# Custom WC (Word Count) Tool

This repository contains a Python script that mimics the functionality of the Unix `wc` command. The script allows you to count the number of bytes, lines, words, and characters in a specified file. It is a lightweight and customizable tool for analyzing text files.

## Features

- **Byte Count**: Count the number of bytes in a file.
- **Line Count**: Count the number of lines in a file.
- **Word Count**: Count the number of words in a file.
- **Character Count**: Count the number of characters in a file.
- **Default Behavior**: If no specific option is provided, the script will output the byte count, line count, and word count by default.

## Usage

To use the script, you need to have Python installed on your system. The script can be run from the command line with various options to specify what you want to count.

### Command Line Options

- `-c`: Outputs the number of bytes in the file.
- `-l`: Outputs the number of lines in the file.
- `-w`: Outputs the number of words in the file.
- `-m`: Outputs the number of characters in the file.
- `-f` or `--file`: Specifies the filename to process.

### Examples

1. **Count Bytes in a File**:
   ```bash
   python custom_wc.py -c -f example.txt
2. **Count Lines in a File**:
   ```bash
   python custom_wc.py -l -f example.txt
3. **Count Words in a File**:
   ```bash
   python custom_wc.py -w -f example.txt
4. **Count Characters in a File**:
   ```bash
   python custom_wc.py -m -f example.txt
5. **Default Behaviour (Count Bytes, Lines, and Words)**:
   ```bash
   python custom_wc.py -f example.txt

## Code Overview

The script is composed of several functions, each responsible for a specific counting task:

- `byteSize(file)`: Counts the number of bytes in the file.
- `countLine(file)`: Counts the number of lines in the file.
- `countWords(file)`: Counts the number of words in the file.
- `countChars(file)`: Counts the number of characters in the file.

The `main()` function handles command-line arguments and invokes the appropriate counting functions based on the provided options.

### Dependencies

- Python 3.x
- `argparse` module (included in the Python standard library)
- `os` module (included in the Python standard library)

## Installation

No installation is required. Simply download the script and run it using Python.

```bash
git clone https://github.com/yourusername/custom-wc.git
cd custom-wc
python custom_wc.py -f example.txt
