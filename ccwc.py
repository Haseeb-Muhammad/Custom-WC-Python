import argparse
import os

def byteSize(file):
    with open(file, 'rb') as f:
        file_size = len(f.read())
        print(f"{file_size} Bytes in {file}")
        return file_size

def countLine(file):
    with open(file, 'r') as f:
        lines = 0
        for line in f:
            lines+=1
        print(f"{lines} lines in {file}")
        return lines

def countWords(file):
    with open(file, 'r') as f:
        words = 0
        for line in f:
            words += len(line.split())
        print(f"{words} words in {file}")
        return words

def countChars(file):
    with open(file, 'r') as f:
        chars = 0
        for line in f:
            chars += len(line)
        print(f"{chars} characters in {file}")
        return chars

def main():
    parser = argparse.ArgumentParser(description="Script for custom Wc")
    
    parser.add_argument("-c", action="store_true", help="c - Outputs the number of bytes in the file")
    parser.add_argument("-l", action="store_true", help="c - Outputs the number of lines in the file")
    parser.add_argument("-w", action="store_true", help="c - Outputs the number of words in the file")
    parser.add_argument("-m", action="store_true", help="c - Outputs the number of characters in the file")
    parser.add_argument("-f", "--file", type=str, help="Filename to process")

    args = parser.parse_args()

    print(f"{args.c}, {args.file}")
    if 

    if not os.path.exists(args.file):
        print(f"{args.file} does not exist")
        return
    else:
        default=True
        if args.c:
            byteSize(args.file)
            default=False
        if args.l:
            countLine(args.file)
            default=False
        if args.w:
            countWords(args.file)
            default=False
        if args.m:  
            countChars(args.file)
            default=False
        if default:
            byteSize(args.file)
            countLine(args.file)
            countWords(args.file)

if __name__ == "__main__":
    main()