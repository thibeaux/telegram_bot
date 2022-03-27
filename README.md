# Telegram Bot
## Overview 
This bot just does some simple command handling, analyzes chat texts trying to match what we say in the chat with Jordan B. Peterson quotes and phrases. Its meant to be a fun joke with my friends. If the bot found a match that someone in the  group used a jordan peterson phrase or quote that is in the word table, it replys to that user and sends a meme in the chat. 

## Commands
* /help to display menu
* /wiki `enter some research keyword` | example: /wiki United States | This will return a summary from wikipedia on the matched keyword

## Chat Analysis, How It Works
The bot will process every chat message sent while the bot program is running. It is polling for Jordan B. Peterson quotes and phrases. The bot will process human input by removing puncuation marks from a message, putting it all on lower case, then finally split the string up by space characters. When we finally have a list of words all lower case with no puncuation we can now start searching. We are going to first look if we can find key words in the phrase bank that was inputted from rthe sent message, and then we are going to append it to a buffer. Once we've finished appending matched keywords to this buffe `phrase_buffer +=key_word # rebuild phrase` we now have a phrase that has been built. Now we can search in the phrase bank for match quotes and phrases. Now, it seems to work better when you leave out useless words like 'the', 'of', 'is', etc. I may look for words like 'bellywhale' instead of ' belly of the whale' because the bot will start to match phrases anytime someone enters 'of' and 'the' which happens a lot. This way we only recognize keywords used in someone's chat message. 

## How to share Ideas and Suggestions
For now, if you have an image link or catchphrase that you want to be added, go ahead and make an issue in the issues section with the quote or urls provided in the desciption. I will get to it as fast as I can. I have a few ideas how to stream line this process. 

If you have a functionality or command suggestion feel free to make issue tickets for that too. 

## Coming Soon
Add database so we can have users add pictures and catchphrases through the bot instead of being manually entered. 

Add youtube command search for keyword searches

Add add meme/picture command so users in chat can send a URL that can be stored in the database for later use

Add command to allow users to make issue tickets and suggestions

Add ability for bot to play music in a call chat (if possible?)
