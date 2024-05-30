import csv
import random

# Open the CSV file
def get_random_words():
    with open("words.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")  # Specify the delimiter (e.g., comma)

        # Read all words from the CSV
        word_list = [row[0] for row in reader]

        # Randomly select three words
        random_words = random.sample(word_list, 3)

        # Combine and print the words
        combined_words = " ".join(random_words)
        return combined_words
"""
this calls the function which concatinates 3 random words from the csv file 
and returns the concatinated string but it does it for 200 times and 
stores all the concatinated strings in a list called random_words
"""
random_words = [get_random_words() for i in range(200)]
