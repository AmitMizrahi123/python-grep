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
        except:  # If no file is used in stdin
            for count_line, line in enumerate(sys.stdin, start=1):  # Loop that run over the lines and counter the lines
                if pattern.search(line):  # Condition that check if just regex in the stdin
                    read.print_with_color(line, file_name_stdin, count_line, pattern)  # We go to the function to print the regex match
                else:
                    print("Regex not found")  # If we dont have regex match we print out Regex not found

    @staticmethod
    def print_with_color(line, file, count_line, pattern):  # This function get 4 arguments and in the end we print the regex match
        lastMatch = 0  # Variable that help us to know where is the regex match end
        formattedText = ''  # Variable that contain the new line
        colourStr = colorama.Fore.RED  # Change the color to red
        resetStr = colorama.Fore.WHITE  # Change the color to white
        for match in pattern.finditer(line):  # Loop over all match regex in line
            start, end = match.span()  # 2 variable that contain the start and end of regex match (span)
            formattedText += line[lastMatch: start]  # We push into the variable the start of the line without the regex match
            formattedText += colourStr  # Switch the color to red for regex
            formattedText += line[start: end]  # Push into the variable the regex match
            formattedText += resetStr  # Switch the color to white for next wards
            lastMatch = end  # Push into the variable the end of regex match
            # Now we rotate to the loop to see if there more regex match
        formattedText += line[lastMatch:]  # Push into the variable the continuation of the line
        print(colored(file, "green") + ": " + colored(count_line, "blue") + ": " + formattedText)  # Print out like grep


if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # Instance of argparse module, use this for take information from user
    parser.add_argument("-r", "--regex", help="Enter a regex string", required=True)  # Create argument for regex this need to be required
    parser.add_argument("-f", "--files", help="Enter a file")  # Create argument parser fot file
    args = parser.parse_args()  # Instance that contain all arguments that we take
    read = MainRegex()  # Instance of our class
    read.main(args.files, args.regex)  # Class to main function inside our class
