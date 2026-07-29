import os
from collections import Counter
from datetime import datetime

LOG_FILE = "execution.log"


# Function to store logs
def write_log(option):
    with open(LOG_FILE, "a") as file:
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        file.write(f"{current_time} --> {option}\n")


# Function to analyze a text file
def analyze_file():

    filename = input("Enter filename from datasets folder: ")

    filepath = os.path.join("datasets", filename)

    if not os.path.exists(filepath):
        print("File not found!")
        return

    with open(filepath, "r") as file:
        text = file.read()

    # Number of characters
    characters = len(text)

    # Number of words
    words = len(text.split())

    # Number of lines
    lines = len(text.splitlines())

    # Number of unique characters
    unique_characters = len(set(text))

    # Letter frequency
    letters = []

    for ch in text:
        if ch.isalpha():
            letters.append(ch.lower())

    frequency = Counter(letters)

    print("\n========== File Analysis ==========")
    print("Characters       :", characters)
    print("Words            :", words)
    print("Lines            :", lines)
    print("Unique Characters:", unique_characters)

    print("\nLetter Frequency")
    print("----------------")

    for letter in sorted(frequency):
        print(letter, ":", frequency[letter])


# Main Menu
while True:

    print("\n========== CryptoLabX ==========")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Attack")
    print("4. Analyze")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        write_log("Encrypt")
        print("Coming Soon")

    elif choice == "2":
        write_log("Decrypt")
        print("Coming Soon")

    elif choice == "3":
        write_log("Attack")
        print("Coming Soon")

    elif choice == "4":
        write_log("Analyze")
        analyze_file()

    elif choice == "5":
        write_log("Exit")
        print("Thank You!")
        break

    else:
        print("Invalid Choice. Try Again.")
