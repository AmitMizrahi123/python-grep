# libraries = [sys, re, argparse, colorama, termcolor]
# sys = to get text from stdin
# re = take regex from user and print all the regex match
# argpare = to deal with the argument
# colorama = help us to see the color
# termcolor, colored = help us to colored the regex match
import sys
import re
import argparse
import colorama
from termcolor import colored

colorama.init()


class MainRegex:
    @staticmethod
    def main(files, regex):
        file_name_stdin = "stdin"  # Send that we work with stdin
        pattern = re.compile(regex, re.MULTILINE)  # Compile the regex
        its_match = 0  # Flag to see if we have regex match
        try:  # Try to catch error if file not open
            with open(files, "r") as file:  # Open the file
                file_name = file.name  # Save the name of file
                for count_line, line in enumerate(file.readlines(), start=1):  # Loop that run over the lines and counter the lines
                    match = pattern.search(line)
                    if match != None:  # Condition that check if we have match for up to one
                        its_match = 1
                    if pattern.search(line):  # Condition that check if just regex in the file
                        read.print_with_color(line, file_name, count_line, pattern)  # We go to the function to print the regex match
                if not its_match:  # Condition that check if not regex match in line to print regex not found
                    print("Regex not found")
                    return
        except:
            for count_line, line in enumerate(sys.stdin, start=1):
                if pattern.search(line):
                    read.print_with_color(line, file_name_stdin, count_line, pattern)
                else:
                    print("Regex not found")

    @staticmethod
    def print_with_color(line, file, count_line, pattern):
        lastMatch = 0
        formattedText = ''
        colourStr = colorama.Fore.RED
        resetStr = colorama.Fore.WHITE
        for match in pattern.finditer(line):
            start, end = match.span()
            formattedText += line[lastMatch: start]
            formattedText += colourStr
            formattedText += line[start: end]
            formattedText += resetStr
            lastMatch = end
        formattedText += line[lastMatch:]
        print(colored(file, "green") + ": " + colored(count_line, "blue") + ": " + formattedText)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--regex", help="Enter a regex string", required=True)
    parser.add_argument("-f", "--files", help="Enter a file")
    args = parser.parse_args()
    read = MainRegex()
    read.main(args.files, args.regex)
