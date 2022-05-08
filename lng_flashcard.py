# Author: Omar
# Importing needed libraries 
import re
import json
import string
import random
import sqlite3
import wikipedia
from flask import Flask, render_template

# Database Class
class db_class:

    # Initializing the datbase's name and the table's name
    def __init__(self):
        self.database_name = './database/lng_vocabulary.db'
        self.table_name = 'vocabulary'
    
    # Creating a method for the database's connector
    def open_db_connection(self):
        self.db_connection = sqlite3.connect(self.database_name)
        self.db_cursor = self.db_connection.cursor()
    
    # Commit the changes to the database and close it
    def close_db_connection(self):
        self.db_connection.commit()
        self.db_connection.close()   
    
    # Creating a table 
    def create_table(self):
        self.open_db_connection()
        self.db_cursor.execute(f"DROP TABLE IF EXISTS {str(self.table_name)}")
        self.db_cursor.execute(f"CREATE TABLE {str(self.table_name)} (original_word TEXT, eng_word TEXT, word_type TEXT, frequency INTEGER)")
        self.close_db_connection()
   
    # Saving/Inserting the words into the database
    def insert_many_records(self, word_corpus):
        self.open_db_connection()
        self.db_cursor.executemany(f"INSERT INTO {str(self.table_name)} VALUES (?,?,?,?)", (word_corpus))
        self.close_db_connection()

    # Lookup 10 random words in the database with a frequency equal to frequency   
    def random_lookup_frequency(self, frequency):
        self.open_db_connection()
        self.db_cursor.execute(f"SELECT original_word FROM {str(self.table_name)} WHERE frequency >= (?) ORDER BY RANDOM() LIMIT 10", (frequency,)) 
        self.items = self.db_cursor.fetchall()
        self.close_db_connection()
        return self.items

# Create database and table object:
db_object = db_class()
db_object.create_table()

# Setting the language and the key words to search in Wikipedia
wikipedia.set_lang("la")
rand_wiki_search =["fructus","translatio","publica","ars","cibus","poetica","amor","familia","mulier","homo","animal","valetudo","natura","color"]

# Searching Wikipedia for random word (defined in rand_wiki_search)  
lng_content = wikipedia.page(random.choice(rand_wiki_search))

# Verify that the content is present if not terminate the program
try:
	scrap_url = lng_content.content
except:
	print('No data was loaded')
	exit()

# Future use for translating each word   
eng_translation = "empty_value"
word_type = "empty_value"

word_histogram = dict()
tuple_corpus = list()

# for loop to split and strip ach line of any punctuation
for line in scrap_url.split():
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    line = line.split()
    # for loop to extract each word from every line and then to assign the word to the word_histogram variable and its number of apperiance
    for word in line:
        if word not in word_histogram:
            word_histogram[word] = 1
        else:
            word_histogram[word] += 1

# for loop to break down the word_histogram into key and value pair with the English translation and the word type (future use)
for key, val in word_histogram.items():
    tuple_corpus.append( (key, eng_translation, word_type, val))

# Calling the insert_many_records method of the db_object and inserting the tuples_corpus' values
db_object.insert_many_records(tuple_corpus)

# Frequency - this will be use as the number of frequency a word appears in page
freq = 3

# Flask app
app = Flask(__name__)

@app.route('/')
def my_view():
    html_file = 'index.html'
    # selecting 10 random words based on the number for frequency and assigning it to the data variable
    data = db_object.random_lookup_frequency(freq)
    # rendering the html and passing the data as json format to the front end
    return render_template(html_file, data=json.dumps(data))

if __name__ == "__main__":
    app.run()
