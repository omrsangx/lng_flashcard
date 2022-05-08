# lng_flashcard

This is a simple web application of a language vocabulary flash card that pull data from Wikipedia, brake each line, separate the words, and then store them in a sqlite3 database and display it based on the number of frequency its appear.

By changing the option to set the language and populating a few keywords of desired target language, you could create a flashcard to practice the vacabulary of any language that is supported under Wikipedia. Sure, I could have used Beautifulsoup or any other scrapping tool and target any website, but I wanted to keep this application simple enough without having to change the source.

Once the data is sent to the front end, the next step is to use Jinga to render the passed data and assign it to the listOfNames variable. With a few lines of JavaScript we are able to use this data and create a carousel. The two functions Next and Prev controls carousel.    

Currently, this application does not check if the word is already in the database. Furthermore, I also wanted to keep the database class simple. 

Author: Omar

# Directory structure:
Parent director
├──────database 
|       |-------lng_vocabulary.db 
| 
├──────templates 
|       └───────index.html 
| 
├──────static 
|       └───────style 
|                └───────style.css 
| 
└──────lng_flashcard.py
                    

