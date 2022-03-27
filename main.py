from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import random
import wikipedia
import API_KEY as bot_key


# telegram.ext reference manuals: https://python-telegram-bot.readthedocs.io/en/stable/index.html
# Reference tutorial: https://www.geeksforgeeks.org/create-a-telegram-bot-using-python/?msclkid=18058a77ad8811ecb17e83ed7842161a

API_KEY = bot_key.api_key # add API KEY here if you don't have one set up in the code
updater = Updater(API_KEY,use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "You've just been infected by cancer lmao")

def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        "/help\n"
        "/gmail <option>\n"
        "/youtube <some search term>\n"
        "/wiki <wiki search>\n"
        "/geeks <geeks4geeks tutorial>"
    )
# TODO: Allow people in the group to write a suggestion, and send me a reminder in chat
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("gmail link here")

#TODO: Allow users to look up youtube videos and possile play audio of youtube videos in voice calls
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("youtube link")


def wiki_lookup(update: Update, context: CallbackContext):
    # reference: https://wikipedia.readthedocs.io/en/latest/code.html
    # https://www.geeksforgeeks.org/wikipedia-module-in-python/?msclkid=5f0988c7adf011eca6429ad117405d5f
    key_word = update.message.text
    key_word = key_word.split(' ', 1)[1]
    print(key_word)
    wikipedia.set_lang("EN")
    try:
        result = wikipedia.summary(key_word,auto_suggest=True)
        update.message.reply_text(result)
    except:
        print(key_word + " does not return anything, try again..")
        update.message.reply_text(key_word + " does not return anything, please try something else..")

#TODO: Allow people in the group to add meme pictures to a database or file
def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text("GeeksforGeeks url here")


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


# Analyze Text in chat below:
def remove_puncuation(inp_str):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    no_punc = ""
    for char in inp_str:
        if char not in punctuations:
            no_punc = no_punc + char

    return no_punc
def get_photo(seed):
    url = [
        "https://i.redd.it/5pjjtdcl9msz.jpg",
        "https://i.redd.it/gqnt7n2r8rd11.jpg",
        "https://i.pinimg.com/originals/9e/f0/40/9ef040f3094d285baafe62801eba1a0d.jpg",
        "http://i0.kym-cdn.com/photos/images/original/001/343/680/3dd.jpg",
        "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1553536954l/44508443.jpg",
        "https://i.ytimg.com/vi/3nHrXmQxBRs/maxresdefault.jpg",
        "https://i.redd.it/7u2ghzkz7p3z.png"
           ]
    random.seed(seed) # help make the choice more random by using user input length as a seed
    index = random.randint(0,len(url)-1)
    print(index)
    return url[index]

def analyze_text(update: Update, context: CallbackContext):
    #variables
    message = update.message.text # takes messages sent in chat and stores it to variable
    word_bank = ['belly','whale', 'lobsters','lobster','dominance', 'hierarchy','hierarchies','collectivists','marxists','marxist',
                 'roughly','speaking','bucko','postmodern', 'neomarxism', 'neomarxist','order','chaos',]
    phrase_bank =['bellywhale', 'lobsters','lobster','dominancehierarchy','collectivists','marxists','marxist',
                  'roughlyspeaking','bucko','postmodernneomarxism','postmodernneomarxist','dominancehierarchies','postmodern','orderchaos',]
    phrase_buffer = ""
    # process input
    lowercase_message = message.lower()
    nopunc_message = remove_puncuation(lowercase_message)
    key_words = nopunc_message.split()# split message to be analyze word for word.

    # parse message for key words and phrases
    for key_word in key_words:
        if key_word in word_bank:
            #print("found a matching word!")
            print(key_word)
            phrase_buffer +=key_word # rebuild phrase
            if phrase_buffer in phrase_bank:
                #print("found a matching phrase!")# debug line
                print(phrase_buffer)
                update.message.reply_text("Jordan B. Peterson notices you ~OwO~")
                update.message.reply_photo(get_photo(len(message))) # using message a seed value

def main():
    # telegram.ext handlers: https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html#handlers
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('wiki', wiki_lookup))
    updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
    updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, analyze_text))
    updater.dispatcher.add_handler(MessageHandler(
        # Filters out unknown commands
        Filters.command, analyze_text))

    # Filters out unknown messages.
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

    #poll for updates and new commands
    updater.start_polling()


if __name__ == '__main__':
    # main code here
    main()
