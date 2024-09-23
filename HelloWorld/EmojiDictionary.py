"""
Name: EmojiDictionary.py
Author: Gavin Hashemi
Date: 2024-09-23 2:11 p.m.
Description:
In geneal rules of thumb, the function should not have print an output or any keyboard input. for this reason, we comment out the 2 lines in below
"""
def emoji_convertor(message):
    #message =  input(">")
    words = message.split(' ')
    emojis = {
        ":)" : "😊",
        ":(" : "🙁",
        ":P" : "😋"
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return(output)
    #print(output)



message = input('Enter a message: ')
print(emoji_convertor(message))
